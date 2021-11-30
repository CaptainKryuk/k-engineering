<template>
  <div class="contact_menu">
    <div class="contact_menu__content">
      <a href="mailto:info@k-engine.ru" class="link nocolor">info@k-engine.ru</a>
      <a href="tel:+74951423418" class="link nocolor">+7 (495) 142-34-18</a>
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