<template>
  <div class="footer">

    <div class="footer__content">

      <div class="footer__content__logo">
        <div class="logo_img">
          <img src="@/assets/img/logo.svg" />
        </div>
        <p class="logo_text">© «К-ИНЖИНИРИНГ». Все права защищены. </p>
      </div>

      <div class="footer__content__sections">
        <div class="footer__content__section" v-for="(section, index) in sections" :key="index">
          <p class="section__title">{{ sections_names[index] }}</p>
          <ul>
            <li v-for="(link, index) in section" :key="index">
              <a :href="link.url" v-if="link.type" target="_blank">{{ link.name }}</a>
              <router-link v-else :to="link.url">{{ link.name }}</router-link>
            </li>
          </ul>
        </div>
      </div>

    </div>

    <div class="footer__bottom">
      <p class="bottom_text">
        Мы используем cookies для сбора обезличенных персональных данных. Они помогают настраивать рекламу и анализировать трафик. Оставаясь на сайте, вы соглашаетесь на сбор таких данных.
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Footer',

  computed: {
    ...mapGetters(['price_list_url']),

    sections() {
      return [this.section1, this.section2, this.section3]
    },

    sections_names() {
      return ['Услуги', "Информация", "Контакты"]
    },

    section1() {
        return[
        {name: 'Каталог', url: '/catalog'},
        {name: 'Прайс-лист', url: this.price_list_url, type: "href"},
        {name: 'Личный кабинет', url: '/lk'},
        {name: 'Реквизиты', url: '/requisites', type: 'href'},
      ]
    },

    section2() {
      return [
        {name: 'Доставка', url: '/delivery'},
        {name: 'О нас', url: '/#about'},
        {name: 'Наши услуги', url: '/#services'},
        {name: 'Подписка на скидки', url: '/#contact'},
      ]
    },

    section3() { 
      return [
        {name: 'info@k-engine.ru', url: 'mailto:info@k-engine.ru', type: "href"},
        {name: 'Москва: +7 (495) 142-34-18', url: 'tel:+74951423418', type: "href"},
        {name: 'Политика обработки персональных данных', url: '/policy'},
      ]
    }
  },

  mounted() {
    console.log(this.price_list_url)
  }
}
</script>