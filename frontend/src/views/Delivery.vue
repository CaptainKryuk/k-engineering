<template>
<contact-menu></contact-menu>

<top-menu></top-menu>

<div class="delivery">
  <breadcrumbs :links="links"></breadcrumbs>

  <div class="delivery__content">
    <div class="delivery__content__menu">
      <div class="menu_elem" v-for="(elem, index) in menu_links" :key="index">
        <a @click="scrollTo(elem.url)" :class="`${elem.status}`">{{ elem.name }}</a>
      </div>
    </div>

    <div class="text_content">
      <h1 id="delivery" style="margin-top: 0">Доставка материалов</h1>

      <h3 id="delivery_mo">Доставка по Москве и Подмосковью</h3>

      <p>
        Доставку по Москве мы осуществляем с помощью сервиса "Яндекс Доставка", что помогает осуществлять доставку быстро и цена значительно ниже, чем через специальные транспортные компании.
        Стоимость зависит от дальности поездки и производится от нашего 
        Документы мы отправляем вместе с материалом. Набор документов стандартный: счет, накладная и счет-фактура.
      </p>

      <h3 id="delivery_city">Доставка в другие города России</h3>

      <p>
        Доставка в другие города осуществляется с помощью <a href="https://www.dellin.ru/" target="_blank">Деловых линий</a> в палетном борту, что обеспечит
        сохранность материала в отличии от деревянной обрешетки, которая дороже и в пути материал может испортиться
      </p>

      <h3 id="delivery_svg">Доставка в страны СНГ</h3>
      <p>
        Доставка в страные СНГ осуществляется по определенной договоренности. Если у Вас есть необходимость в ней - просьба связаться с нами по телефону +7 (495) 142-34-18
        или Вы можете написать нам на нашу электронную почту info@k-engine.ru
      </p>

      <h3 id="delivery_price">Стоимость доставки</h3>

      <p>
        Стоимость доставки зависит от дальности конечного пункта

        <ul>
          <li>Доставка по москве и московской области - от 1000 (В пределах МКАД) до 2000 рублей (Северное подмосковье: Одинцово/Щелково и т.д.)</li>
          <li>Доставка в другие города России - в среднем около 1500 рублей, также зависит от конечного пункта доставки</li>
          <li>Доставка в другие страны СНГ - договорная</li>
        </ul>
      </p>

      <h3 id="delivery_date">Сроки доставки</h3>

      <p>
        Отправка заказа осуществляется на следующий рабочий после оформления заявки, если заявка была создана до 14:00 по московскому времени,
        Если после 14:00, то через один рабочий день.<br/>
        При больших заказах может потребоваться один рабочий день для подготовки отгрузки и для вызова машины от "Деловых линий"
      </p>

      <h3 id="delivery_free">Бесплатная доставка</h3>

      <p>
        Бесплатная доставка осуществляется от суммы в 40 000 рублей
      </p>

      <h3 id="delivery_problems">Проблемы с товаром</h3>

      <p>
        При получении товара в рулонах не всегда есть возможность все сто метров проверить на наличие заводского брака, 
        поэтому при возникновении неприятных ситуаций, мы берем ответственность на себя и готовы предоставить новый материал без брака или вернуть деньги.
        Также мы берем ответственность за доставку материалов по Москве и МО, и если при получении Вы обнаружили брак, который не обнаружили мы перед отправкой, мы также отправим
        Вам новый материал или вернем деньги
      </p>

      <h1 id="delivery_pickup">Самовывоз</h1>

      <p>
        Вы можете забрать заказ на следующий день после оформления заказа после 12:00 по адресу: Московская область, Горки Ленинские, Западная улица, 19
      </p>

      <h1 id="delivery_express">
        Экспресс-доставка
      </h1>

      <p>
        Экпресс-доставка осуществляется в пределах Москвы и МО и может быть осуществлена в день оформления заказа, если заказ оформлен до 12:00. скидки на Экспресс-доставку при заказе от 40 000 
        не предоставляются. Стоимость экспресс-доставки - стоимость доставки + 1500 рублей
      </p>
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
        {name: 'Доставка', link: ''}
      ],

      menu_links: [
        {name: 'Доставка', url: 'delivery', status: 'h1'},
        {name: 'Доставка по Москве и Подмосковью', url: 'delivery_mo', status: 'h3'},
        {name: 'Доставка в другие города России', url: 'delivery_city', status: 'h3'},
        {name: 'Доставка в страны СНГ', url: 'delivery_svg', status: 'h3'},
        {name: 'Стоимость доставки', url: 'delivery_city', status: 'h3'},
        {name: 'Сроки доставки', url: 'delivery_date', status: 'h3'},
        {name: 'Бесплатная доставка', url: 'delivery_free', status: 'h3'},
        {name: 'Проблемы с товаром', url: 'delivery_problems', status: 'h3'},
        {name: 'Самовывоз', url: 'delivery_pickup', status: 'h1'},
        {name: 'Экспресс-доставка', url: 'delivery_express', status: 'h1'},
      ]
    }
  },

  mounted() {
    document.title = 'Доставка | К-инжиниринг' 
  },

  methods: {
    scrollTo(id) {
      let elem = document.getElementById(id)
      console.log(elem.offsetTop)
      window.scrollTo({
        top: elem.offsetTop - 50,
        behavior: 'smooth'
      })
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>