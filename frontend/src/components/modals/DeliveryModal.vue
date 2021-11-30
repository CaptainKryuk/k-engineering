<template>
<modal-window>
  <div class="modal__close" @click="$emit('close')">
    <img src="@/assets/img/close--black.svg" width="42" height="42" alt="" />
  </div>



</modal-window>
</template>

<script>
import Modal from '@/components/ModalWindow.vue'

export default {
  name: "DeliveryModal",

  components: {
    'modal-window': Modal
  },

  props: {
    'title': String,
    'show': Boolean,
  }

}
</script>
