<template>
  <router-view/>

  <toast-container></toast-container>
</template>
<script>
import Toasts from '@/components/Toasts'

export default {
  name: 'App',

  components: {
    'toast-container': Toasts
  },

  data() {
    return {
      show: false
    }
  },

  mounted() {
    setTimeout(() => {
      this.show = true
    }, 500)

  }
}
</script>
<style lang="sass">
@mixin font($fname, $fstyle, $fweight, $furl)
  @font-face
    font-family: $fname
    font-style: $fstyle
    font-weight: $fweight
    // font-display: swap // Uncomment to initially display system fonts
    src: local($fname), url($furl) format('woff2')

@include font('Lato', normal, 300, './assets/fonts/Lato/Lato-Light.ttf')
@include font('Lato', normal, 400, './assets/fonts/Lato/Lato-Regular.ttf')
@include font('Lato', normal, 500, './assets/fonts/Lato/Lato-Medium.ttf')
@include font('Lato', normal, 700, './assets/fonts/Lato/Lato-Bold.ttf')
@include font('Lato', normal, 800, './assets/fonts/Lato/Lato-Heavy.ttf')

// montseratt
@include font('Montserrat', normal, 300, './assets/fonts/Montserrat/Montserrat-Light.ttf')
@include font('Montserrat', normal, 400, './assets/fonts/Montserrat/Montserrat-Regular.ttf')
@include font('Montserrat', normal, 500, './assets/fonts/Montserrat/Montserrat-Medium.ttf')
@include font('Montserrat', normal, 600, './assets/fonts/Montserrat/Montserrat-SemiBold.ttf')
@include font('Montserrat', normal, 700, './assets/fonts/Montserrat/Montserrat-Bold.ttf')
@include font('Montserrat', normal, 800, './assets/fonts/Montserrat/Montserrat-Black.ttf')

.route-enter-from
  opacity: 0
  transform: translateX(100px)

.route-enter-active 
  transition: all 0.3s ease-out

.route-leave-to
  opacity: 0
  transform: translateX(-100px)

.route-leave-active
  transition: all 0.3s ease-in

body
  margin: 0

#app
  font-family: 'Montserrat', sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  padding: 0
  margin: 0
  scroll-behavior: smooth
  text-rendering: optimizeLegibility
</style>
