<template>

<div class="top_menu">
  <div class="top_menu__icon mobile">
    <img src="@/assets/img/menu--mobile.svg" width="32" height="32" alt="icon_menu" @click="show_menu = true" />  
  </div>

  <div class="top_menu__logo">
    <img src="@/assets/img/tagline-logo.svg" @click="routeTo('/')" />
  </div>

  <div class="top_menu__elems desktop">
    <div class="top_menu__elems__detail" v-for="(el, index) in links" :key="index">
      <router-link :to="el.url" :class="['link', el.classes]" v-if="el.classes !== 'download'">{{ el.name }}</router-link>
      
      <a :href="el.url" target="_blank" class="link download" v-if="el.classes === 'download'">{{ el.name }}</a>
    </div>
  </div>
</div>

<!-- sidebar menu -->
<transition name="leftslide">
  <div :class="['sidebar_menu']" v-if="show_menu">
      <div class="sidebar_menu__box" >
        <div class="sidebar_menu__top">
          <div class="sidebar_logo">
            <img src="@/assets/img/logo.svg" width="160" height="40" />
          </div>
          <div class="sidebar_close">
            <img src="@/assets/img/close--black.svg" width="32" height="32" @click="show_menu = false" />
          </div>
        </div>

        <div class="sidebar_menu__content">
          <router-link class="sidebar_item_detail" 
              v-for="(item, index) in links"
              :to="item.url"
              :key="index">
            <div class="sidebar_item_icon">
              <img :src="`/static/img/${item.icon}.svg`" width="26" height="26"/>
            </div>
            <p class="sidebar_item_text">{{ item.name }}</p>
          </router-link>
        </div>
      </div>
  </div>
</transition>

<transition name="rightslide" appear>
  <div class="sidebar_menu__shadow" v-if="show_menu" @click="show_menu = false"></div>
</transition>


</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: "TopMenu",

  data() {
    return {
      show_menu: false
    }
  },

  computed: {
    ...mapGetters(['price_list_url']),

    links() {
        return [
        {name: 'Главная', url: '/', icon: 'catalog'},
        {name: 'Каталог', url: '/catalog', icon: 'catalog'},
        {name: 'Доставка', url: '/delivery', icon: 'catalog'},
        {name: 'Прайс-лист', url: this.price_list_url, classes: 'download', icon: 'price-list'},
        {name: 'Личный кабинет', url: '/lk', icon: 'lk', classes: 'btn_link blocked'}
      ]
    } 
  },

  methods: {
    routeTo(link) {
      this.$router.push(link)
    }
  }
}
</script>