<template>
  <div class="toasts_container">
    <!-- all existed notification -->
    <transition-group
      name="float"
      tag="div"
      appear
    >
      <div
        v-for="toast in toasts"
        :key="toast"
        :class="['toast', toast.status]"
      >
        <div class="icon">
          <img :src="`/static/img/toasts/${toast.status}.svg`">
        </div>

        <div class="text">
          <p class="toast_title">
            {{ toast.title }}
          </p>

          <p class="toast_desc">
            {{ toast.message }}
          </p>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: "Toast",

  data() {
    return {

    }
  },

  computed: {
    ...mapState(['toasts'])
  },

  methods: {
  }
}
</script>

<style scoped lang="sass">
@import "@/assets/sass/style.sass"
</style>