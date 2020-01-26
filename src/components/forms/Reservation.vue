<template>
  <div class="m-reservation">
    <h4 class="uk-h4 uk-heading-line"><span>Бронирование</span></h4>
    <div class="uk-text-center" v-if="status === 'ok'">
      <h5>
        Ваша заявка отправлена!
      </h5>
      <p>
        В ближайшее время с вами свяжется администратор гостевого дома "Маяк".
      </p>
      <button class="uk-button uk-button-primary" v-on:click="sendAgain">
        Отправить снова
      </button>
    </div>
    <form class="uk-form-stacked" v-on:submit.prevent="reservation" v-else>
      <div class="uk-margin">
        <label class="uk-form-label" for="start_date">Дата заезда</label>
        <div class="uk-form-controls">
          <input class="uk-input" v-model="booking.start_date" name="start_date" id="start_date" type="date" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="end_date">Дата отъезда</label>
        <div class="uk-form-controls">
          <input class="uk-input" v-model="booking.end_date" name="end_date" id="end_date" type="date" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="persons">Кол-во человек</label>
        <select class="uk-select" v-model="booking.persons" name="persons" id="persons">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9+</option>
        </select>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="first_name">Ваше имя</label>
        <div class="uk-form-controls">
          <input class="uk-input" v-model="booking.first_name" name="first_name" id="first_name" placeholder="Иван"
                 type="text" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="phone">Ваш телефон</label>
        <div class="uk-form-controls">
          <input class="uk-input" v-model="booking.phone" name="phone" id="phone" type="text"
                 placeholder="+7 999 999-99-99" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="email">Ваш email</label>
        <div class="uk-form-controls">
          <input class="uk-input" v-model="booking.email" name="email" id="email" type="email"
                 placeholder="ivanov@mail.ru" required>
        </div>
      </div>
      <div class="uk-margin uk-text-center">
        <button type="submit" class="uk-button uk-button-primary uk-width-1-1" v-if="!loading">Забронировать</button>
        <div uk-spinner v-else></div>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        name: 'reservation',
        data: () => ({
            loading: false,
            status: null,
            booking: {
                first_name: null,
                phone: null,
                email: null,
                start_date: null,
                end_date: null,
                persons: null
            }
        }),
        methods: {
            async reservation () {
                this.loading = true
                await this.$axios.post('/api/bookings/reservation/', this.booking)
                    .then(r => {
                        this.loading = false
                        this.status = r.data.status
                    })
                    .catch(e => {
                        this.loading = false
                        console.dir(e)
                    })
            },
            sendAgain () {
                this.booking = {
                    first_name: null,
                    phone: null,
                    email: null,
                    start_date: null,
                    end_date: null,
                    persons: null
                }
                this.status = null
            }
        }
    }
</script>

<style scoped>

</style>
