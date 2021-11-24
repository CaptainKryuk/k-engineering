import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

let app = createApp(App)

app.config.globalProperties.$axios = axios

// add global components
import inputs from '@/components/inputs'

let components = [...inputs]
components.forEach(component => {
  app.component(component.name, component)
})


// directives
app.directive('click-outside', {
    beforeMount(el, binding) {
      el.clickOutsideEvent = function (event) {
        // here I check that click was outside the el and his childrens
        // console.log(el, event.target)
        if (el==event.target) {
          // Если кликнули на элемент на котором записана директива
        }
        
        if (el.contains(event.target)) {
          // если кликнули на элемент, который находится внутри директивы
        }
        if (!(el===event.target || el.contains(event.target))) {
          // console.log('click on background')
          // вызов функции, переданной через имя в директиву
          binding.value()
        }
      };
      document.body.addEventListener('click', el.clickOutsideEvent)
    },
    unmounted: function (el) {
      document.body.removeEventListener('click', el.clickOutsideEvent)
    }
})
  
app.config.productionTip = false
  
app.use(store).use(router).mount('#app')
