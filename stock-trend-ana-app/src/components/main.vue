<template>
  <el-container>
    <el-aside>
      <el-menu :default-active="this.$route.path" class="siderbar" mode="vertical" @select="handleSelect" router
        background-color="#409EFF" text-color="#C0C4CC" active-text-color="#fff">
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
          { path: '/index', navItem: 'INDEX', disabled: false, icon: 'el-icon-data-line' },
          { path: '/news', navItem: 'NEWS', disabled: false, icon: 'el-icon-postcard' },
          { path: '/support', navItem: 'HELP!!', disabled: true, icon: 'el-icon-help' },
          { path: '/about', navItem: 'ABOUT', disabled: false, icon: 'el-icon-user' },
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
  .navName {
    font-family: Microsoft YaHei;

  }

  .el-menu-item i {
    color: #C0C4CC;
  }

  .el-aside {
    padding-top: 50px;
    background-color: #409EFF;
    text-align: center;
    line-height: 200px;
    width: 200px !important;
    height: 500px;
  }

  .el-main {
    background-color: #ecf0f4;
    color: #333;
    text-align: center;
    padding-bottom: 0px;
  }

  .el-menu {
    border-right: none;
  }
</style>