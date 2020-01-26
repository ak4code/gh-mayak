import Vue from 'vue'
import './plugins/axios'
import UIkit from 'uikit'
import '@/assets/styles/styles.scss'
import Icons from 'uikit/dist/js/uikit-icons'
import Reservation from './components/forms/Reservation'
import FeedbackForm from './components/forms/FeedbackForm'

Vue.config.productionTip = false
UIkit.use(Icons)

const app = new Vue({
  el: '#app',
  components: {
    Reservation,
    FeedbackForm,
  }
})
