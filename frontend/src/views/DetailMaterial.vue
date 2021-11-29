<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="material" v-if="Object.keys(material).length">
  <breadcrumbs :links="links"></breadcrumbs>

  <div class="material__top">
    <h1>Переплетный материал Balacron {{ material.collection.name }} {{ material.item_number }}</h1>

    <div class="material__top__buttons">
      <button class="btn btn_icon nofill">
        <img src="@/assets/img/share--accent.svg" />
        В избранное
      </button>

      <button class="btn btn_icon nofill">
        <img src="@/assets/img/like--accent.svg" />
        Поделиться
      </button>
    </div>
  </div>

  <div class="material__content">
    <div class="material__content__avatar">
      <div class="material_avatar">
        <img :src="`${server_media}catalog/high/${getImgId()}`" width="500" height="500" alt="" />
      </div>
    </div>

    <div class="material__content__features">
      <div class="material_feature" v-for="(material, index) in features" :key="index">
        <p class="feature_name">{{ material.name }}</p>
        <span class="feature_divider"></span>
        <p class="feature_result">{{ material.result }}</p>
      </div>

    </div>

    <div class="material__content__price">

      <div class="price_box">
        <div class="price_box__top">
          <p class="price_box__top__text">Цена за 1 погонный метр</p>
          <div class="price_box__top__img">
            <img src="@/assets/img/question--gray.svg" />
          </div>
        </div>

        <p class="price_box__price">
          {{ material.collection.price1 }} <span class="rub">₽</span>
        </p>

        <div class="price_box__existance">
          <p :class="['price_box__existance_text', material.quantity]"></p>
          <div class="price_box__existance__img">
            <img src="@/assets/img/question--gray.svg" />
          </div>
        </div>

        <button class="btn btn_icon nofill">
          <img src="@/assets/img/notification--accent.svg" />
          Узнавать о скидках
        </button>

        <button class="btn btn_border full" @click="show_modal = true">Связаться с менеджером</button>
      </div>

      <div class="price_underbox">
        <button class="btn btn_icon glow">
          <img src="@/assets/img/box--accent.svg" />
          Экспресс-доставка
        </button>

        <p class="underbox_hint">Что такое экспресс-доставка?</p>
      </div>
    </div>
  </div> 

  
  <div class="material__other">
    <p class="material__other__title">Другие цвета коллекции {{ material.collection.name }}</p>

    <div class="material__other__list">
      <div class="other__list__detail" v-for="(mat, index) in other_collections" :key="index" @click="routeTo(`/materials/${mat.item_number}`)">
        <div class="detail__avatar">
          <div class="empty_img" v-if="!mat.img">
              <img src="@/assets/img/sad-smile--gray.svg" width="30" height="30"/>
              <span>Не найдено</span>
          </div>
          <img :src="`${server_media}catalog/low/${getImgId(mat)}`" v-if="mat.img" width="120" height="120" alt="" />
        </div>
        <div class="detail__text">{{ mat.item_number }}</div>
      </div>
    </div>
  </div>

</div>

<order-modal :material="getMaterialName()" 
             :show="show_modal" 
             title="Оформить заказ" 
             v-if="Object.keys(material).length"
             @close="show_modal = false"></order-modal>

<my-footer></my-footer>
</template>

<script>
import ContactMenu from '../components/ContactMenu.vue'
import Breadcrumbs from '../components/Breadcrumbs.vue'
import TopMenu from '../components/TopMenu.vue'
import Footer from '../components/Footer.vue'
import OrderModal from '../components/modals/OrderModal.vue'
import { mapState } from 'vuex'

export default {
  name: "DetailMaterial",

  components: {
    'contact-menu': ContactMenu,
    'top-menu': TopMenu,
    'breadcrumbs': Breadcrumbs,
    'my-footer': Footer,
    'order-modal': OrderModal
  },

  data() {
    return {
      links: [
        {name: 'Главная', link: '/'},
        {name: 'Каталог', link: '/catalog'},
        {name: 'Atelier', link: ''}
      ],

      material: {},
      other_collections: [],

      show_modal: false,
    }
  },

  computed: {
    ...mapState(['server', 'server_media']),

    features() {
      if (Object.keys(this.material).length) {
        return [
          {name: 'Коллекция', result: this.material.collection.name},
          {name: 'Серия', result: this.material.collection.series.name},
          {name: 'Цвет', result: this.material.color},
          {name: 'Материал', result: "Винил"},
          {name: 'Размер', result: this.material.collection.size},
          {name: 'Плотность', result: '270 g/m'},
          {name: 'Артикул', result: this.material.item_number},
        ]
      }
      return []
    },

    route_item() {
      return this.$route.params.item
    }
  },

  watch: {
    'route_item': {
      handler() {
        this.getMaterial()
      }
    }
  },

  mounted() {
    this.getMaterial()
  },

  methods: {

    getMaterialName() {
      return `${this.material.collection.name} ${this.material.item_number}`
    },

    getMaterial() {
      if (this.$route.params.item) {
        this.$axios.get(`${this.server}material/${this.$route.params.item}`)
          .then((response) => {
            this.material = response.data
            this.links[2] = {name: `${response.data.collection.name} ${response.data.item_number}`, link: ''}
            this.getOtherMaterials(response.data.collection.name)
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },

    getOtherMaterials(collection) {
      this.$axios.get(`${this.server}catalog/${collection}/`)
        .then((response) => {
          let data = []
          for (let i=0; i<response.data.length; i++) {
            if (String(response.data[i].item_number) !== String(this.$route.params.item)) {
              data.push(response.data[i])
            }
          }
          this.other_collections = data
        })
    },
    
    getImgId(material) {
      let detail_material = material ? material : this.material
      if (detail_material?.img) {
        return detail_material?.img.split('catalog/')[1]
      }
      return null

    },

    routeTo(link) {
      this.$router.push(link)
      this.$forceUpdate()
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>