<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="catalog">
  <div class="catalog__top">
    <breadcrumbs :links="links" />
    
    <div class="catalog__title">
      <h1>Каталог</h1>
      <h2>Переплетные материалы Балакрон</h2>
    </div>

    <div class="catalog__filter">
      <div class="filter_search">
        <text-input v-model="item_number"
                    placeholder="Артикул"
                    icon="search--gray"
                    type="number" />
      </div>

      <div class="filter_select">

        <select-input v-model="collection"
                      :options="['Все серии', 'ATELIER', 'HERITAGE', 'SPECTRUM', 'TEXTILE', 'METALLIC']"
                      icon="collection"
                      placeholder="Серия"></select-input>

        <select-input v-model="design"
                      :options="filtered_collections"
                      icon="design"
                      placeholder="Коллекция"></select-input>

        <button class="btn btn_icon search" style="height: 50px">
          <img src="@/assets/img/search--white.svg" />
          Найти
        </button>
      </div>
      
    </div>

  </div>

  <div class="catalog__content">
    <div class="material__list" v-if="Object.keys(catalog).length && !loading">
      <div class="material__list_wrapper" v-for="(material, index) in filtered_catalog" :key="index">
        <div class="material__list__detail" @click="routeTo(`/materials/${material.item_number}`)">

          <div class="detail_img">
            <img :src="`${server_url}/media/catalog/low/${getImgId(material)}`" width="155" height="155" alt="alt" v-if="material.img" />

            <div class="absent__img" v-if="!material.img">
              <img src="@/assets/img/sad-smile--gray.svg" width="36" height="36"/>
              <span>Не найдено</span>
            </div>
          </div>

          <div class="detail_content">
            <div class="detail_content__info">
              <p class="bold">{{ material.collection.name }}</p>
              <p>Цвет</p>
              <p>Размер</p>
            </div>

            <div class="detail_content__result">
              <p>{{ material.item_number }}</p>
              <p>{{ material.color }}</p>
              <p>{{ material.collection.size }}</p>
            </div>
          </div>

          <div class="detail_bottom">
            <button class="btn_circle_icon like" @click="test"></button>
            <button class="btn_circle_icon cart" @click="routeTo(`/materials/${material.item_number}`)"></button>
          </div>

        </div>
      </div>
    </div>

    <!-- loading -->
    <div class="material__list loading" v-if="loading">

      <div class="spinner"></div>
      <div class="material__list_wrapper" v-for="i in Array(8).length" :key="i">
        <div class="material__list__detail mock">
          <div class="detail_img mock"></div>
        </div>
        <div class="detail_content"></div>

      </div>
    </div>

    <!-- cant find something -->
    <div class="not_found" v-if="catalog.length && !filtered_catalog.length">
      <div class="not_found__content">
        <div class="not_found__content__icon">
          <img src="@/assets/img/absent-table.svg" />
        </div>

        <div class="not_found__content__text">
          <h3>Материал не найден</h3>
          <p>Материал с выбранными параметрами отсутствует, Вы можете попробовать выбрать другие параметры или связаться с нами, чтобы решить Ваш вопрос</p>
        </div>

        <div class="not_found__content__bottom">
          <button class="btn round" @click="resetFilter()">Сбросить</button>
          <button class="btn_link">Связаться с менеджером</button>
        </div>
      </div>
    </div>
  </div>
</div>

  <my-footer></my-footer>
</template>

<script>
import Breadcrumbs from '../components/Breadcrumbs.vue'
import ContactMenu from "../components/ContactMenu.vue"
import Footer from "../components/Footer.vue"
import TopMemu from "../components/TopMenu.vue"
import { mapMutations, mapState } from 'vuex'

export default {

  components: { 
    'contact-menu': ContactMenu, 
    'breadcrumbs': Breadcrumbs,
    'top-menu': TopMemu,
    'my-footer': Footer
  },

  name: 'Catalog',

  data() {
    return {
      links: [
        {name: 'Главная', link: '/'},
        {name: 'Каталог', link: ''}
      ],

      item_number: '',
      collection: 'Все серии',
      design: '',

      catalog: [],

      loading: false
    }
  },

  computed: {
    ...mapState(['server', 'server_url',]),

    filtered_catalog() {
      return this.catalog.filter((material) => {
        if (!material.item_number.includes(this.item_number)) {
          return false
        }

        if (this.collection.length && this.collection !== 'Все серии') {
          if (this.collection !== material.collection.series.name) {
            return false
          }
        }

        if (this.design.length && this.design !== 'Все') {
          if (this.design !== material.collection.name) {
            return false
          }
        }
        return true
      })
    },

    filtered_collections() {
      let collections = { 
        "HERITAGE": [ "Masanti", "Figary", "Algora", "Merino", "Tanarto", "Orinoco", "Istrana", "Lipare", "Macanet" ], 
        "SPECTRUM": [ "Casina", "Ismara", "Fluctuations", "Capys", "Marano", "Reflections", "Magister" ], 
        "ATELIER": [ "Tango", "Mettalix Astrakhan", "Walnut", "Croco", "Calabria", "Padusa", "Maple", "Metallix Beaudiva", "Dust" ], 
        "TEXTILE": [ "Imperial", "Tsarina crush", "Savanna", "Imperial CP", "Rexa laminated", "Coloret laminated" ], 
        "METALLIC": [ "Galaxy" ] 
      }
      if (this.collection.length) {
        this.design = ''
        if (this.collection !== 'Все серии') {
          return collections[this.collection]
        }

      }
      return [ "Masanti", "Figary", "Algora", "Merino", "Tanarto", "Orinoco", "Casina", "Ismara", "Maple", "Imperial", "Tango", "Mettalix Astrakhan", "Walnut", "Tsarina crush", "Croco", "Calabria", "Padusa", "Istrana", "Lipare", "Macanet", "Fluctuations", "Capys", "Marano", "Savanna", "Imperial CP", "Reflections", "Magister", "Rexa laminated", "Coloret laminated", "Galaxy", "Metallix Beaudiva", "Dust" ]
    },
  },

  mounted() {
    this.getCatalog()

    if (this.$route.params.collection) {
      this.collection = this.$route.params.collection.toUpperCase()
      this.INFO_TOAST({'title': `Выбрана коллекция ${this.$route.params.collection.toUpperCase()}`, 'text': "Выбрана определенная коллекция, Вы можете выбрать Все серии выбрав этот пункт в выпадающем фильтре"})
    }
  },

  methods: {
    ...mapMutations(['DANGER_TOAST', 'SUCCESS_TOAST', 'INFO_TOAST']),

    test(e) {
      if (e) {
        e.stopPropagation()
      }
    },

    getCatalog() {
      this.loading = true
      this.$axios.get(`${this.server}catalog/`)
        .then((response) => {
          this.catalog = response.data
          this.loading = false
        })
    },


    resetFilter() {
      this.design = ''
      this.item_number = ''
      this.collection = 'Все серии'
    },

    getImgId(material) {
      if (material.img) {
        return material.img.split('catalog/')[1]
      }

      return null
    },

    routeTo(link) {
      this.$router.push(link)
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>