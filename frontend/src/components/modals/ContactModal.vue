<template>
<modal-window :show="show" :title="title" @close="$emit('close')">
  <div class="modal__close" @click="$emit('close')">
    <img src="@/assets/img/close--black.svg" width="42" height="42" alt="" />
  </div>
  <form @submit.prevent="sendRequest()">
    <text-input field_name="Ваше имя или компания" 
                v-model="name" 
                :required="true" 
                placeholder='Например: "ООО К-инжиниринг"' />

    <text-input field_name="Телефон или электронная почта" 
                v-model="contact" 
                :required="true"
                placeholder='Например: info@k-engineering.ru' />


    <button type="submit" class="btn btn_border full" style="border-radius: 40px">Оставить заявку</button>

    <p class="hint">
      Нет времени на заявку? Позвоните нам по номеру 
      <a href="tel:+7 496 999-99-99">+7 496 999-99-99</a> 
      или напишите на  нашу электронную почту 
      <a href="mailto:info@k-engineering.ru">info@k-engineering.ru</a>
    </p>
  </form> 
</modal-window>
</template>

<script>
import Modal from '@/components/ModalWindow.vue'
import { mapMutations, mapState } from 'vuex'

export default {
  /*
  Это окно необходимо для отправки каких-либо заявок из выпадающих окон
  содержить поле "Имя или название компании" и поле телефон или Email 
  */
  name: "ContactModal",

  components: {
    'modal-window': Modal
  },
  
  props: {
    'title': String,
    'show': Boolean
  },

  data() {
    return {
      name: '',
      contact: ''
    }
  },

  computed: {
    ...mapState(['server'])
  },

  methods: {
    ...mapMutations(['SUCCESS_TOAST', 'DANGER_TOAST']),

    sendRequest() {
      const mail_re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
      const phone_re = /^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/im

      let flag = false

      if (this.contact.match(mail_re)) {
        flag = true
      } else if (this.contact.match(phone_re)) {
        flag = true
      } 

      if (!flag) {
        this.DANGER_TOAST({title: 'Ошибка при заполнении', text: 'Электронная почта или телефон введены неверно, проверьте корректность введенных данных'})
      } else {
        this.$axios.post(`${this.server}subscribe/`,
          {
            name: this.name,
            contact: this.contact
          })
          .then((response) => {
            this.$emit('close')
            this.SUCCESS_TOAST({title: "Заявка отправлена", text: "Заявка на звонок отправлена, мы перезвоним Вам в течении 10 минут"})
          })
      }

    }
  }
}
</script>