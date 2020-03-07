<template>
  <div class="feedback-form">
    <div class="uk-flex uk-flex-wrap uk-flex-middle uk-flex-between">
      <div><h3 class="uk-margin-remove">Здесь вы можете оставить свой отзыв</h3></div>
      <div>
        <button class="uk-button uk-button-primary" uk-toggle="target: #feedback-form">Написать</button>
        <div id="feedback-form" uk-modal>
          <div class="uk-modal-dialog uk-modal-body">
            <button class="uk-modal-close-default" type="button" uk-close></button>
            <form class="uk-form-stacked uk-dark" v-on:submit.prevent="sendFeedback">
              <div class="uk-margin">
                <label class="uk-form-label" for="name">Ваше Имя</label>
                <div class="uk-form-controls">
                  <input class="uk-input" v-model="feedback.name" name="name" id="name" type="text" required>
                </div>
              </div>
              <div class="uk-margin">
                <label class="uk-form-label" for="city">Город</label>
                <div class="uk-form-controls">
                  <input class="uk-input" v-model="feedback.city" name="city" id="city" type="text" required>
                </div>
              </div>
              <div class="uk-margin">
                <label class="uk-form-label" for="text">Ваш отзыв</label>
                <div class="uk-form-controls">
                  <textarea class="uk-textarea" v-model="feedback.text" name="text" id="text" required
                            rows="5"></textarea>
                </div>
              </div>
              <div class="uk-align-right">
                <button class="uk-button-primary uk-button">Отправить</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <ul class="uk-comment-list uk-width-1-1">
      <li v-for="feed in feedback_list" :key="feed.id" class="uk-margin">
        <article class="uk-comment uk-margin-small">
          <header class="uk-comment-header uk-grid-medium uk-flex-middle" uk-grid>
            <div class="uk-width-expand">
              <h5 class="uk-comment-title uk-text-small uk-margin-remove">{{feed.name}}</h5>
              <ul class="uk-comment-meta uk-text-small uk-subnav uk-subnav-divider uk-margin-remove-top">
                <li><span>{{feed.created_at}}</span></li>
                <li><span>{{feed.city}}</span></li>
                <li v-if="isAuth === 'True'">
                  <button class="uk-button uk-button-small uk-button-text" v-on:click="answer(feed.id)">Ответить
                  </button>
                </li>
              </ul>
            </div>
          </header>
          <div class="uk-comment-body">
            <p class="uk-text-small">{{feed.text}}</p>
          </div>
        </article>
        <ul v-if="feed.answers" class="uk-margin">
          <li v-for="answer in feed.answers" :key="answer.id" class="uk-margin">
            <article class="uk-comment uk-comment-answer uk-margin-small">
              <header class="uk-comment-header uk-grid-medium uk-flex-middle" uk-grid>
                <div class="uk-width-expand">
                  <h5 class="uk-comment-title uk-text-small uk-margin-remove">{{answer.name}}</h5>
                  <ul class="uk-comment-meta uk-text-small uk-subnav uk-subnav-divider uk-margin-remove-top">
                    <li><span>{{answer.created_at}}</span></li>
                    <li><span>{{answer.city}}</span></li>
                  </ul>
                </div>
              </header>
              <div class="uk-comment-body">
                <p class="uk-text-small">{{answer.text}}</p>
              </div>
            </article>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
    import UIkit from 'uikit'

    export default {
        name: "feedback-form",
        props: ['isAuth'],
        data: () => ({
            feedback_list: [],
            feedback: {
                name: null,
                city: null,
                text: null,
                feedback: null
            }
        }),
        created () {
            this.getFeedbackList()
        },
        methods: {
            async getFeedbackList () {
                await this.$axios.get('/api/feedback/')
                    .then(r => {
                        this.feedback_list = r.data
                    })
                    .catch(e => {
                        console.dir(e)
                    })
            },
            async sendFeedback () {
                await this.$axios.post('/api/feedback/send/', this.feedback)
                    .then(this.renew())
                    .catch(e => {
                        console.dir(e)
                    })
            },
            answer (id) {
                this.feedback = {
                    name: 'Гостевой дом "Маяк"',
                    city: 'Голубицкая',
                    text: null,
                    feedback: id
                }
                UIkit.modal(document.getElementById('feedback-form')).show()
            },
            async renew () {
                await this.getFeedbackList()
                this.feedback = {
                    name: null,
                    city: null,
                    text: null,
                    feedback: null
                }
                UIkit.modal(document.getElementById('feedback-form')).hide()
            }
        }
    }
</script>

<style scoped>

</style>
