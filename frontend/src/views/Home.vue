<template>
<transition name="fade" appear>
<section v-show="loaded">

<contact-menu></contact-menu>

<!-- sidebar menu -->
<transition name="leftslide">
  <div :class="['sidebar_menu']" v-if="show_menu">
      <div class="sidebar_menu__box" >
        <div class="sidebar_menu__top">
          <div class="sidebar_logo">
            <img src="@/assets/img/tagline-logo.svg" width="160" height="60" />
          </div>
          <div class="sidebar_close">
            <img src="@/assets/img/close--black.svg" width="32" height="32" @click="show_menu = false" />
          </div>
        </div>

        <div class="sidebar_menu__content">
          <div class="sidebar_item_detail" 
              v-for="(item, index) in menu"
              :key="index"
              @click="routeTo(item.url, href=item.type === 'download' ? true : false)">
            <div class="sidebar_item_icon">
              <img :src="`/static/img/${item.icon}.svg`" width="26" height="26"/>
            </div>
            <p class="sidebar_item_text">{{ item.name }}</p>
          </div>
        </div>
      </div>
  </div>
</transition>

<transition name="rightslide" appear>
  <div class="sidebar_menu__shadow" v-if="show_menu" @click="show_menu = false"></div>
</transition>



<div class="top">
  <div class="top__background">
    <img src="/static/img/top/img1.jpg" width="204" height="22" alt=""/>
    <div class="white_background"></div>
  </div>

  <!-- mobile menu -->
  <div class="top__menu">
    <div class="menu_icon mobile">
      <img src="@/assets/img/menu--mobile.svg" width="36" height="36" alt="" @click="show_menu=true" />
    </div>
    <div class="logo">
      <img src="@/assets/img/logo.svg" width="250" height="90"/>
    </div>
  </div>

  <div class="top__content">

    <div class="desktop_menu_icon" @click="show_menu = true">
      <img src="@/assets/img/menu--mobile.svg" width="48" height="48" @click="show_menu=true" />
    </div>

    <!-- desktop -->
    <div class="top__content__slideshow">
      <div class="movebtn left" id="move_left"></div>
      <div class="movebtn right" id="move_right"></div>
      <swiper
        :slides-per-view="1"
        :space-between="50"
        parallax
        :pagination="{clickable: false}"
        :navigation="{nextEl: '#move_right', prevEl: '#move_left'}"
        :autoplay="{autoplay: true, delay: 3000}"
        :zoom="true">

        <swiper-slide v-for="i in Array(3).length" :key="i">
          <div class="slideshow_img">
            <img :src="`/static/img/top/img${i}.jpg`" /> 
          </div>
        </swiper-slide>
      </swiper>
    </div>

    <div class="top__content__text">

      <div class="top__content__text__menu">
        <div class="logo">
          <img src="@/assets/img/logo.svg" width="220"/>
        </div>
        <div class="menu_icon mobile">
          <img width="36" height="36" src="@/assets/img/menu--mobile.svg" alt="" @click="show_menu=true" />
        </div>
      </div>
      
      <h1>Переплетные материалы</h1>
      <h2>Balacron International</h2>
      <p>Balacron International - первый в мире производитель бумаги с 
      виниловым покрытием. Мы занимаемся поставкой материалов BN 
      international более 25 лет и имеем огромный опыт работы с фабриками</p>

      <div class="content_buttons">
        <button class="btn arrow" style="margin-right: 25px" @click="routeTo('/catalog')">Каталог</button>
        <button class="btn btn_icon glow" @click="routeTo(price_list_url, href=true)">
          <img src="@/assets/img/price-list--accent.svg" />
          Прайс-лист
        </button>
      </div>

    </div>

  </div>
</div>


<div class="materials">

  <swiper
    :slides-per-view="1"
    :space-between="50"
    parallax
    :pagination="{clickable: false}"
    :navigation="{nextEl: '#move_material_right', prevEl: '#move_material_left'}">

    <swiper-slide v-for="(material, index) in materials" :key="index">

      <div class="materials__box">
        <div class="materials__box__top">
          <p class="text">переплетные материалы</p>

          <div class="arrows desktop">
            <img src="@/assets/img/arrow--left--gray.svg" id="move_material_left" width="56" height="16" />
            <img src="@/assets/img/arrow--right--gray.svg" id="move_material_right" width="56" height="16" />
          </div>
        </div>

        <div class="materials__box__content">
          <div class="content__description">
            <p class="materials__box__title">{{ material.name }}</p>
            <p class="materials__box__subtitle">Balacron</p>
            <p class="materials__box__text">
              {{ material.text }}
            </p>

            <div class="action_buttons">
              <button class="btn_circle_icon plus" @click="routeTo(`/catalog/${material.name.toLowerCase()}`)"></button>
            </div>

            <div class="arrows mobile">
              <img src="@/assets/img/arrow--left--black.svg" id="move_material_left" width="56" height="16"/>
              <img src="@/assets/img/arrow--right--black.svg" id="move_material_right" width="56" height="16" />
            </div>

            <div class="images">
              <div class="material_img">
                <img :src="`/static/img/materials/${material.name.toLowerCase()}/2.jpg`" alt="" width="160" height="360" />
              </div>
              <div class="material_img">
                <img :src="`/static/img/materials/${material.name.toLowerCase()}/1.jpg`" alt="" width="160" height="360" />
              </div>
            </div>

            <button :class="['btn', 'arrow', !is_desktop ? 'full' : '']" @click="routeTo(`/catalog/${material.name.toLowerCase()}`)">Выбрать</button>
          </div>

          <!-- on desktop -->
          <div class="content__slides">
            <div class="material_img">
                <img :src="`/static/img/materials/${material.name.toLowerCase()}/1.jpg`" alt="" width="250" height="400" />
            </div>
            <div class="material_img blocked">
              <img :src="`/static/img/materials/${material.name.toLowerCase()}/2.jpg`" alt="" width="250" height="400" />
            </div>
          </div>

        </div>

      </div>
    </swiper-slide>
  </swiper>



</div>

<div class="home_menu" id="about">
  <div class="home_menu__list">
    <div class="home_menu__detail" 
      v-for="(el, index) in small_menu" 
      :key="index">
      <p :class="['menu_elem', index === 0 ? 'selected' : '']" @click="routeTo(el.url)">{{ el.name }}</p>

      <p class="menu_text" v-if="index === 0">
        К-инжиниринг - первая компания в России, начавшая поставлять Голландские материалы Balacron в Россию.
        Мы занимаемся поставкой материалов уже более 25 лет и являемся официальными дистрибьюторами материалов Balacron.
        <br/><br/>
        Основной проблемой при закупках импортного материала является отсутствие нужной коллекции в наличии, 
        необходимо его заказывать из Европы и ждать более двух месяцев,
        у нас в наличии более 150 позиций, а заказ Вы сможете получить уже на следующий день.
        <br/><br/>
        Мы принимаем заказы любых размеров и готовы обеспечить поставку материала в кратчайшие сроки.
      </p>
    </div>
  </div>

  <div class="home_menu__content">
    <p>      
      К-инжиниринг - первая компания в России, начавшая поставлять Голландские материалы Balacron в Россию.
      Мы занимаемся поставкой материалов уже более 25 лет и являемся официальными дистрибьюторами материалов Balacron.
      <br/><br/>
      Основной проблемой при закупках импортного материала является отсутствие нужной коллекции в наличии, 
      необходимо его заказывать из Европы и ждать более двух месяцев,
      у нас в наличии более 150 позиций, а заказ Вы сможете получить уже на следующий день.
      <br/><br/>
      Мы принимаем заказы любых размеров и готовы обеспечить поставку материала в кратчайшие сроки.
    </p>
  </div>
</div>

<div class="section service" id="services">
  <h2 class="section__title">Наши услуги</h2>
  <p class="section__subtitle">Что мы делаем для наших клиентов</p>

  <div class="service__list">
    <div class="service__detail" v-for="(service, index) in services" :key="index">
      <div class="service__detail__box">
        <div class="card_avatar">
          <img :src="`/static/img/${service.icon}--accent.svg`" />
        </div>

        <p class="card_title">{{ service.title }}</p>
        <p class="card_text">{{ service.text }}</p>
        <div class="card_footer">
          <button class="btn arrow" @click="routeTo(service.url)">{{ service.button }}</button>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="section contact" id="contact">
  <p class="contact__title">
    Узнавайте о скидках и выгодных предложениях первыми
  </p>
    <form @submit.prevent="addSubscribe()">
      <div class="contact__content">

        <div class="input">
          <input v-model="email" type="email" required placeholder="Введите ваш email" />
        </div>
        <button :class="['btn', !is_desktop ? 'full' : '']" type="submit">Подписаться</button>

      </div>
    </form>

  <div class="contact__footer">
    <div class="divider"></div>

    <img src="@/assets/img/logo.svg" width="204" height="80" alt="" />
  </div>
</div>

</section>
</transition>


</template>

<script>
import ContactMenu from '@/components/ContactMenu.vue'
// import Swiper core and required modules
import SwiperCore, { Navigation, Pagination, Scrollbar, A11y, Autoplay, Parallax } from 'swiper';
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';
// Import Swiper styles
import 'swiper/swiper.scss';
import 'swiper/components/navigation/navigation.scss';
import 'swiper/components/pagination/pagination.scss';
import 'swiper/components/scrollbar/scrollbar.scss';
import { mapGetters, mapMutations, mapState } from 'vuex';

// install Swiper modules
SwiperCore.use([Navigation, Pagination, Scrollbar, A11y, Autoplay, Parallax]);

export default {
  name: 'Home',

  components: {
    'contact-menu': ContactMenu,
    Swiper,
    SwiperSlide
  },

  data() {
    return {
      materials: [
        {id: 0, name: 'heritage', text: 'Коллекция Heritage из натурального льна обладает идеальной тактильностью, которая поможет почувствовать текстуру под кончиками пальцев. Яркие цвета и необычные фактуры придадут вашим изделиям новый, эксклюзивный вид'},
        {id: 1, name: 'spectrum', text: 'Сила цветов безгранична. Он рассказывает историю, он дает возможность показать, кто вы есть, он дает обзор. Держись или свобода, разум или эмоции. Выбор за вами. Спектр дает вам свободу выбора.'},
        {id: 2, name: 'atelier', text: 'Сила воображения, движимая десятилетиями опыта и любопытства. Игра в инновации и дизайн. Результат раздвигания границ и раздвигания их. Снова и снова. С Atelier вы можете создавать продукты, которые задают тон будущему'},
        {id: 3, name: 'textile', text: 'Текстиль - это текстильный покровный материал с широким спектром возможностей. Тиснение фольгой, слепое тиснение, трафаретная печать. Текстиль придает естественный вид и дышит уважением.'}
      ],

      selected_material: 0,

      small_menu: [
        {name: 'О нас', icon: 'about', url: '/about'},
        {name: 'Личный кабинет', icon: 'lk', url: '/lk'},
        {name: 'Наши услуги', icon: 'services', url: '#services'},
        {name: 'Свяжитесь с нами', icon: 'contact', url: '#contact'}
      ],

      services: [
        {title: 'Подберите материал', text: 'Подберите материал для ваших изделий и получите его уже на следующий день. Весь материал, представленный в каталоге в наличии', icon: 'cart', button: 'Каталог', url: '/catalog'},
        {title: 'Личный кабинет', text: 'Отслеживание заказа, система скидок, персонализация и удобный функционал для быстрого получения нужного вам материала', icon: 'chart', button: 'Войти', url: '/lk'},
        {title: 'Решается все', text: 'Возникли вопросы при заказе? Нужен материал в день заказа? Напишите или позвоните нам, мы моментально решим все вопросы в течении часа', icon: 'laptop', button: 'Написать', url: '#contact'}
      ],

      email: '',

      show_menu: false,
      show_contact: false,
      loaded: true
    }
  },

  computed: {
    ...mapState(['server']),
    ...mapGetters(['price_list_url']),

    selected_materials() {
      return this.materials.filter((mat) => mat.id === this.selected_material)
    },

    is_desktop() {
      return window.screen.width > 1200
    },

    menu() {
      return [
        {name: 'Каталог', icon: 'catalog', url: '/catalog'},
        {name: 'Прайс-лист', icon: 'price-list', url: this.price_list_url, type: "download"},
        {name: 'О нас', icon: 'about', url: '#about'},
        {name: 'Личный кабинет', icon: 'lk', url: '/lk'},
        {name: 'Наши услуги', icon: 'services', url: '#services'},
        {name: 'Свяжитесь с нами', icon: 'contact', url: '#contact'}
      ]
    }
  },

  methods: {
    ...mapMutations(['SUCCESS_TOAST', 'DANGER_TOAST']),
    
    previousImg() {
      if (this.materials[this.selected_material - 1]) {
        return this.materials[this.selected_material - 1].name
      } else {
        return this.materials[this.materials.length - 1].name
      }
    },

    addSubscribe() {
      const mail_re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

      if (this.email.match(mail_re)) {
        this.$axios.post(`${this.server}subscribe/`,
          {'contact': this.email})
          .then((response) => {
            this.email = ''
            window.scrollTo({
              top: 0,
              behavior: 'smooth'
            })
            this.SUCCESS_TOAST({title: 'Вы успешно подписались', text: 'Вы успешно подписались на рассылку скидок, Вам будут приходить только оповещения о скидках'})
          })
          .catch((error) => {
            this.DANGER_TOAST({title: "Ошибка во время запроса", text: 'Произошла ошибка во время выполнения запроса, мы уже ее заметили и пытаемся исправить'})
          })
      } else {
        this.DANGER_TOAST({title: "Неверно введен E-mail", text: 'Введен некорректный E-mail, проверьте правильно ли введена Ваша электронная почта'})
      }


    },

    nextImg() {
      if (this.materials[this.selected_material + 1]) {
        return this.materials[this.selected_material + 1].name
      } else {
        return this.materials[0].name
      }
    },

    nextMat() {
      if (this.selected_material === 3) {
        this.selected_material = 0
      } else {
        this.selected_material++
      }
      this.$forceUpdate()
    },

    previousMat() {
      if (this.selected_material === 0) {
        this.selected_material = 3
      } else {
        this.selected_material--
      }
      this.$forceUpdate()
    },

    closeMenu() {
      this.show_menu = false
    },

    routeTo(link, href=false) {
      this.show_menu = false
      if (href) {
        window.open(link)
      } else {
        this.$router.push(link)
      }
    },
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>