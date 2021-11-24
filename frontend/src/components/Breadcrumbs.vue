<template>
<div class="breadcrumbs">
  <div class="breadcrumbs__links">
    <span class="breadcrumbs__link" v-for="(link, index) in links" :key="index">
      <router-link :to="`${link.link}`">{{ link.name }}</router-link>
    </span>
  </div>
</div>
</template>

<script>
export default {
  name: "Breadcrumbs",

  props: {
    'links': Array
  },

  data() {
    return {

    }
  }
}
</script>