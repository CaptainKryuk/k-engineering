<template>
  <label class="text_input">
    <div class="text_input__icon" v-if="icon">
      <img :src="`/static/img/${icon}.svg`" width="18" height="18" alt="icon" />
    </div>

    <div class="text_input__content">
      <input :type="type"
             :value="modelValue"
             @input="$emit('update:modelValue', $event.target.value)"
             class="placeholder"
             :placeholder="placeholder"  />
    </div>
  </label>
</template>

<script>
export default {
  name: 'text-input',

  props: {
    'modelValue': String,
    'placeholder': String,
    'required': Boolean,
    'icon': String,
    'type': {
      type: String,
      default: 'text'
    }
  },

  data() {
    return {

    }
  }
}
</script>