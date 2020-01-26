<template>
  <div class="feedback-form">
    <div class="uk-flex uk-flex-wrap uk-flex-middle uk-flex-between">
      <div><h3 class="uk-margin-remove">Здесь вы можете оставить свой отзыв</h3></div>
      <div>
        <button class="uk-button uk-button-primary" uk-toggle="target: #feedback-form">Написать</button>
        <div id="feedback-form" uk-modal>
          <div class="uk-modal-dialog uk-modal-body">
            <button class="uk-modal-close-default" type="button" uk-close></button>
            <form class="uk-form-stacked uk-dark">
              <div class="uk-margin">
                <label class="uk-form-label" for="name">Ваше Имя</label>
                <div class="uk-form-controls">
                  <input class="uk-input" name="name" id="name" type="text" required>
                </div>
              </div>
              <div class="uk-margin">
                <label class="uk-form-label" for="city">Город</label>
                <div class="uk-form-controls">
                  <input class="uk-input" name="city" id="city" type="text" required>
                </div>
              </div>
              <div class="uk-margin">
                <label class="uk-form-label" for="text">Ваш отзыв</label>
                <div class="uk-form-controls">
                  <textarea class="uk-textarea" name="text" id="text" required rows="5"></textarea>
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
    <div class="uk-width-1-1">
      <article class="uk-comment" v-for="feed in feedback_list" :key="feed.id">
        <header class="uk-comment-header uk-grid-medium uk-flex-middle" uk-grid>
          <div class="uk-width-expand">
            <h5 class="uk-comment-title uk-text-small uk-margin-remove">{{feed.name}}</h5>
            <ul class="uk-comment-meta uk-text-small uk-subnav uk-subnav-divider uk-margin-remove-top">
              <li><span>{{feed.created_at}}</span></li>
              <li v-if="isAuth"><a href="#">Ответить</a></li>
            </ul>
          </div>
        </header>
        <div class="uk-comment-body">
          <p class="uk-text-small">{{feed.text}}</p>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
    export default {
        name: "feedback-form",
        props: ['isAuth'],
        data: () => ({
            feedback_list: [],
            feedback: {
                name: null,
                city: null,
                text: null
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
            }
        }
    }
</script>

<style scoped>

</style>
