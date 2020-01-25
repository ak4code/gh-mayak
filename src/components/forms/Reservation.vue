<template>
  <div class="m-reservation">
    <h4 class="uk-h4 uk-heading-line"><span>Бронирование</span></h4>
    <form class="uk-form-stacked">
      <div class="uk-margin">
        <label class="uk-form-label" for="start_date">Дата заезда</label>
        <div class="uk-form-controls">
          <input class="uk-input" name="start_date" id="start_date" type="date" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="end_date">Дата отъезда</label>
        <div class="uk-form-controls">
          <input class="uk-input" name="end_date" id="end_date" type="date" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="persons">Кол-во человек</label>
        <select class="uk-select" name="persons" id="persons">
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
          <input class="uk-input" name="first_name" id="first_name" placeholder="Иван" type="text" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="phone">Ваш телефон</label>
        <div class="uk-form-controls">
          <input class="uk-input" name="phone" id="phone" type="text" placeholder="+7 999 999-99-99" required>
        </div>
      </div>
      <div class="uk-margin">
        <label class="uk-form-label" for="phone">Ваш email</label>
        <div class="uk-form-controls">
          <input class="uk-input" name="email" id="email" type="email" placeholder="ivanov@mail.ru" required>
        </div>
      </div>
      <div class="uk-margin">
        <button type="submit" class="uk-button uk-button-primary uk-width-1-1">Забронировать</button>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        name: "reservation",
        methods: {}
    }
</script>

<style scoped>

</style>
