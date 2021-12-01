<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="info_section">
  <breadcrumbs :links="links"></breadcrumbs>

  <h1 class="section__title">
    Наши реквизиты
  </h1>

  <div class="info_section__content">
    <div class="info_section__content__text">
      <p>Наименование: ИП "КРЮКОВ АНДРЕЙ АЛЕКСАНДРОВИЧ"</p>
      <p>ИНН: 500913948021</p>
      <p>ОГРН: 321508100438559</p>

      <h3>Реквизиты банка</h3>

      <p>Наименование: АО «Тинькофф Банк»</p>
      <p>Юридический адрес: 127287, г. Москва, ул. Хуторская 2-я, д. 38А, стр. 26</p>
      <p>Рассчетный счет: 30232810100000000004</p>
      <p>Корр. счет: 30101810145250000974 в ГУ Банка России по ЦФО</p>
      <p>БИК: 044525974</p>
      <p>ИНН: 7710140679</p>
      <p>КПП: 771301001</p>
      <p>Код по ОКПО: 29290881</p>
    </div>

    <div class="info_section__content__map">
      <h3>Наш склад на карте</h3>

      <p>Наша почта: info@k-engine.ru</p>
      <p>Наш номер телефона: +7 (495) 142-34-18</p>

      <div id="map" style="width: 600px; height: 400px"></div>
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

export default {
  name: "DetailMaterial",

  components: {
    'contact-menu': ContactMenu,
    'top-menu': TopMenu,
    'breadcrumbs': Breadcrumbs,
    'my-footer': Footer,
  },

  data() {
    return {
      links: [
        {name: 'Главная', link: '/',},
        {name: 'Реквизиты', link: ''}
      ],
    }
  },

  mounted() {
    document.title = 'Реквизиты | К-инжиниринг' 
  },

  methods: {
    installMap() {
      
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>