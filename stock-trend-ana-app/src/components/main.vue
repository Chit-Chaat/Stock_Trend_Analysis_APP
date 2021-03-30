<template>
  <el-container>
    <el-aside>
      <el-menu :default-active="this.$route.path" class="siderbar" mode="vertical" @select="handleSelect" router
        background-color="#fff" text-color="#333" active-text-color="#0084ff">
        <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.path" :disabled="item.disabled">
          <template slot="title">
            <i :class="item.icon"></i>
            <span class="navName"> {{ item.navItem }}</span>
          </template>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main class="content">
      <router-view />
    </el-main>
  </el-container>

</template>

<script>
  export default {

    data() {
      return {
        navList: [
          { path: '/index', navItem: 'Index', disabled: false, icon: 'el-icon-data-line' },
          { path: '/news', navItem: 'News', disabled: false, icon: 'el-icon-postcard' },
          { path: '/support', navItem: 'Help!!', disabled: true, icon: 'el-icon-help' },
          { path: '/about', navItem: 'About', disabled: false, icon: 'el-icon-user' },
        ]

      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);

      }
    }
  }
</script>

<style scoped>
  .sidebar {}

  .content {}

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
    width: 200px !important;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
  }

</style>