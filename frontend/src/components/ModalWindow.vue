<template>
<div class="modal" v-show="show">
  <transition name="fade" appear>
    <div class="modal__shadow" v-show="show" @click="$emit('close')"></div>
  </transition>

  <transition name="fade" appear>
    <div class="modal__window" v-show="show">
      <div class="modal__window__title">
        <p>{{ title }}</p>
      </div>
      <div class="modal__window__content">
        <slot></slot> 
      </div>

    </div>
  </transition>

</div>
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
  }
}
</script>