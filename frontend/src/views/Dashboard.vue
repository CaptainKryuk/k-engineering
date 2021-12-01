<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="lk">
  <breadcrumbs :links="links" />

  <div class="lk__content">
    <div class="lk__content__box">
      <div class="lk__content__icon">
        <img src="@/assets/img/no_lk.svg" />
      </div>

      <h1>Личный кабинет в режиме тестирования</h1>
      <p>Личный кабинет недоступен так как его функционал находится в режиме тестирования, заказы пока оформляются напрямую</p>

      <router-link to="/catalog" class="btn round">Посмотреть наш каталог</router-link>
    </div>

  </div>
</div>

<my-footer></my-footer>
</template>

<script>
import ContactMenu from '../components/ContactMenu.vue'
import Breadcrumbs from '../components/Breadcrumbs.vue'
import TopMenu from '../components/TopMenu.vue'
import Footer from '../components/Footer.vue'
import { mapState } from 'vuex'

export default {
  name: "DetailMaterial",

  components: {
    'contact-menu': ContactMenu,
    'top-menu': TopMenu,
    'breadcrumbs': Breadcrumbs,
    'my-footer': Footer,
  },

  computed: {
    links() {
      return [
        {name: 'Главная', link: '/'},
        {name: 'Каталог', link: '/catalog'},
        {name: 'Личный кабинет', link: ''},
      ]
    }
  }, 

  mounted() {
    document.title = 'Личный кабинет | К-инжиниринг' 
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>