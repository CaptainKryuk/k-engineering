<template>
  <transition name="fade">
    <div class="modal" v-show="show">

        <div class="modal__shadow" @click="close"></div>

        <div class="modal__window">
          <div class="modal__window__title">
            <p>{{ title }}</p>
          </div>
          <div class="modal__window__content">
            <slot></slot> 
          </div>

        </div>

    </div>

  </transition>
</template>

<script>
export default {
  name: "ModalWindow",

  props: {
    'title': String,
    'show': Boolean
  },

  data() {
    return {}
  },

  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>