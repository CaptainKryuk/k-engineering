import { createStore } from 'vuex'

export default createStore({
  state: {
    server: process.env.NODE_ENV === 'development' ? "http://127.0.0.1:8000/api/" : "https://k-engineering.ru/api/",
    server_static: process.env.NODE_ENV === 'development' ? "http://127.0.0.1:8000/static/" : "https://k-engineering.ru/static/",
    server_media: process.env.NODE_ENV === 'development' ? "http://127.0.0.1:8000/media/" : "https://k-engineering.ru/media/",

    server_url: process.env.NODE_ENV === 'development' ? "http://127.0.0.1:8000" : "https://k-engineering.ru",
    // toasts
    toasts: [],
  },
  mutations: {

    DANGER_TOAST(state, args) {
      state.toasts.unshift({
        'message': args.text,
        'title': args.title,
        'status': 'warning'
      })
  
      setTimeout(() => {
        state.toasts.pop()
      }, 5000)
    },
  
    SUCCESS_TOAST(state, args) {
      state.toasts.unshift({
        'message': args.text,
        'title': args.title,
        'status': 'success'
      })
  
      setTimeout(() => {
        state.toasts.pop()
      }, 5000)
    },

    INFO_TOAST(state, args) {
      state.toasts.unshift({
        'message': args.text,
        'title': args.title,
        'status': 'info'
      })
  
      setTimeout(() => {
        state.toasts.pop()
      }, 5000)
    }
  },
  actions: {
  },
})
