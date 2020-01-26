from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.generic import ListView, TemplateView
from .models import Photo, Booking, Feedback
from .serializers import BookingSerializer, FeedbackSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class PhotosListView(ListView):
    model = Photo
    template_name = 'hotel/photo_list.html'


class FeedbackListView(TemplateView):
    template_name = 'hotel/feedback_list.html'


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, permission_classes=[AllowAny], methods=['post'])
    def reservation(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_booking(serializer.data)
            return Response({'status': 'ok'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


def send_booking(booking):
    subject = 'Бронирование на сайте azov-mayak.ru'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = settings.DEFAULT_TO_EMAIL
    template_html = render_to_string('hotel/email_booking.html', {
        'booking': booking
    })
    template_text = render_to_string('hotel/email_booking.txt', {
        'booking': booking
    })
    msg = EmailMultiAlternatives(subject, template_text, from_email, [to], reply_to=[booking['email']])
    msg.attach_alternative(template_html, "text/html")
    msg.send()
