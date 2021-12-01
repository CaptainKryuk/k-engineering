<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="material" v-if="Object.keys(material).length">
  <breadcrumbs :links="links"></breadcrumbs>

  <div class="material__top">
    <h1>Переплетный материал Balacron {{ material.collection.name }} {{ material.item_number }}</h1>

    <div class="material__top__buttons">
      <button class="btn btn_icon nofill" @click="toFavorites()">
        <img src="@/assets/img/like--accent.svg" />
        В избранное
      </button>

      <button class="btn btn_icon nofill" @click="copyLink()">
        <img src="@/assets/img/share--accent.svg" />
        Скопировать ссылку
      </button>
    </div>
  </div>

  <div class="material__content">
    <div class="material__content__avatar">
      <div class="material_avatar">
        <div class="empty_img" v-if="!material.img">
          <img src="@/assets/img/sand-clock--gray.svg" width="46" height="46" alt=""/>
          <span>Будет позже</span>
        </div>

        <img :src="`${server_media}catalog/high/${getImgId()}`" width="500" height="500" alt="" class="img" v-if="material.img" />
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
          <p class="price_box__top__text">Цена от 100 погонных метров</p>
          <div class="price_box__top__img hover_price" hover_info>
            <img src="@/assets/img/question--gray.svg" />
          </div>
        </div>

        <p class="price_box__price">
          {{ material.collection.price2 }} <span class="rub">₽</span>
        </p>

        <div class="price_box__existance">
          <p :class="['price_box__existance_text', material.quantity]"></p>
          <div class="price_box__existance__img hover_existance" hover_info>
            <img src="@/assets/img/question--gray.svg" />
          </div>
        </div>

        <button class="btn btn_icon nofill" @click="show_appear = true">
          <img src="@/assets/img/notification--accent.svg" />
          Сообщить о наличии
        </button>

        <button class="btn btn_border full" @click="show_modal = true">Связаться с менеджером</button>
      </div>

      <div class="price_underbox">
        <button class="btn btn_icon glow" @click="routeTo('/delivery#delivery_express')">
          <img src="@/assets/img/box--accent.svg" />
          Экспресс-доставка
        </button>

        <p class="underbox_hint" @click="routeTo('/delivery#delivery_express')">Что такое экспресс-доставка?</p>
      </div>
    </div>
  </div> 

  
  <div class="material__other">
    <p class="material__other__title">Другие цвета коллекции {{ material.collection.name }}</p>

    <div class="material__other__list">
      <div class="other__list__detail" v-for="(mat, index) in other_collections" :key="index" @click="routeTo(`/materials/${mat.item_number}`)">
        <div class="detail__avatar">
          <div class="empty_img" v-if="!mat.img">
              <img src="@/assets/img/sand-clock--gray.svg" width="30" height="30"/>
              <span>Будет позже</span>
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

<appear-modal :material="getMaterialName()"
              :show="show_appear"
              title="Подписаться на появление материала в наличии"
              v-if="Object.keys(material).length"
              @close="show_appear = false"></appear-modal>

<my-footer></my-footer>
</template>

<script>
import ContactMenu from '../components/ContactMenu.vue'
import Breadcrumbs from '../components/Breadcrumbs.vue'
import TopMenu from '../components/TopMenu.vue'
import Footer from '../components/Footer.vue'
import OrderModal from '../components/modals/OrderModal.vue'
import { mapMutations, mapState } from 'vuex'
import AppearModal from '../components/modals/AppearModal.vue'

export default {
  name: "DetailMaterial",

  components: {
    'contact-menu': ContactMenu,
    'top-menu': TopMenu,
    'breadcrumbs': Breadcrumbs,
    'my-footer': Footer,
    'order-modal': OrderModal,
    'appear-modal': AppearModal
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
      show_appear: false,
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
          {name: 'Материал', result: this.material.item_number.length > 4 ? 'Винил' : 'Ткань'},
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
    document.title = 'Материал | К-инжиниринг' 
  },

  methods: {
    ...mapMutations(['INFO_TOAST', 'SUCCESS_TOAST']),

    getMaterialName() {
      return `${this.material.collection.name} ${this.material.item_number}`
    },

    toFavorites() {
      this.INFO_TOAST({title: "Материал добавлен", text: "Материал добавлен в избранное, он будет отображаться первым"})
    },

    copyLink() {
      this.$copyText(`https://k-engine.ru${this.$route.fullPath}`)
      this.SUCCESS_TOAST({title: "Ссылка на материал скопирована", text: "Ссылка на материал сохранена в Вашем буфере обмена, Вы можете вставить ее с помощью Ctrl+V"})
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