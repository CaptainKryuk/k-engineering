<template>
  <label class="custom_input">
    <p class="field_name" v-if="field_name">{{ field_name }}</p>

    <div :class="['text_input', disabled ? 'disabled' : '']" >
      <div class="text_input__icon" v-if="icon">
        <img :src="`/static/img/${icon}.svg`" width="18" height="18" alt="icon" />
      </div>

      <div class="text_input__content">
        <input :type="type"
              :value="modelValue"
              :required="required"
              @input="$emit('update:modelValue', $event.target.value)"
              class="placeholder"
              :placeholder="placeholder"
              :disabled="disabled"  />
      </div>
    </div>

  </label>
</template>

<script>
export default {
  name: 'text-input',

  props: {
    'modelValue': {
      type: [String, Number]
    },
    'placeholder': String,
    'disabled': {
      type: Boolean,
      default: false
    },
    'required': Boolean,
    'icon': String,
    'type': {
      type: String,
      default: 'text'
    },
    'field_name': String
  },

  data() {
    return {

    }
  }
}
</script>