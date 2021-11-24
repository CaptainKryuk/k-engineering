<template>
<div class="select_input">
    <div class="custom_select" v-click-outside="closeSelect">

      <div class="parent_block" @click="show_fold_menu = !show_fold_menu">
        <div class="parent_block__content">
          <div class="icon" v-if="icon">
            <img :src="`/static/img/${icon}.svg`" />
          </div>
          <p class="text" v-if="modelValue">{{ modelValue }}</p>
          <p class="placeholder" v-if="!modelValue">{{ placeholder }}</p>
        </div>

        <div class="icon" v-if="show_fold_menu" @click="test()">
          <img src="/static/img/arrow--up--gray.svg" />
        </div>
        <div class="icon" v-if="!show_fold_menu" @click="test()">
          <img src="/static/img/arrow--down--gray.svg" />
        </div>
      </div>

      <div class="fold_block" v-if="show_fold_menu">
        <div :class="['block', isValueEqualField(option) ? 'selected' : '']" 
             v-for="(option, index) in options" 
             :key="index"
             @click="selectValue(option)">
          <div class="text">{{ option }}</div>
          <div class="icon"><img src="@/assets/img/check--gray.svg" v-if="isValueEqualField(option)"/></div>
        </div>
      </div>
    </div>

</div>
</template>

<script>
export default {
  name: "select-input",
  
  props: {
    "modelValue": String, 
    "options": Array,
    "required": {
      type: Boolean,
      default: false
    },
    'placeholder': String,
    'icon': String,
  },
  
  data() {
    return {
      show_fold_menu: false,
    }
  },
  
  methods: {
    closeSelect() {
      this.show_fold_menu = false
    },

    test() {
      this.show_fold_menu = !this.show_fold_menu
    },

    getFieldValue() {
      for (let i=0; i<this.options.length; i++) {
        if (this.options[i] === this.modelValue) {
          return this.options[i]
        }
      }
    },

    isValueEqualField(value) {
      if (value === this.modelValue) {
        return true
      }
      return false
    },

    selectValue(option) {
      this.$emit('update:modelValue', option)
      this.closeSelect()
    }
  },

}
</script>