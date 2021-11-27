<template>
  <div class="contact_menu">
    <div class="contact_menu__content">
      <a href="mailto:andrey.kryukov@deploy-x.com" class="link nocolor">andrey.kryukov@deploy-x.com</a>
      <a href="tel:+79653316711" class="link nocolor">+7 (965) 331-67-11</a>
      <span class="link" @click="show_contact = true">Связаться с нами</span>
    </div>
  </div>

  <contact-modal :show="show_contact" title="Заказать звонок" @close="show_contact = false"></contact-modal>
</template>

<script>
import ContactModal from '@/components/modals/ContactModal.vue'

export default {
  name: "ContactMenu",
  
  components: {
    'contact-modal': ContactModal
  },

  data() {
    return {
      show_contact: false
    }
  }
}
</script>