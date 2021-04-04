<template>
  <el-container id="app">
    <div id="cover"></div>
    <el-header>
      <Header></Header>
    </el-header>
    <el-container>
      <el-container>
        <el-main>
          <Main></Main>
        </el-main>
        <el-footer>
          <Footer></Footer>
        </el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
  import Header from './components/header.vue'
  import Footer from './components/footer.vue'
  import Main from './components/main.vue'
  export default {
    name: 'index',
    components: {
      Header,
      Main,
      Footer,
      
    },
    data() {
      return {
        title: {
          main_title: "Stock Trend Analysis APP",
          sub_title: "DSCI 560",
          desc: "Using Knowledge Graph techniques help you find the most suitable school, and start your new life."
        }
      }
    }
  }
</script>

<style scoped>
  #app {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
  }

  #cover {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: rgb(199, 199, 199);
    opacity: 0.20;
    z-index: -1;
  }

  .el-header{
    width: 100%;
    height: 80px !important;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 80px;
  }

  .el-main {
    background-color: #ecf0f4;
    color: #333;
    text-align: center;
    height: 500px;
    padding: 0 !important;
  }

  .el-footer {
    width: 100%;
    height: 150px !important;
    color: #333;
    line-height: 120px;
    padding: 0 !important;
  }
</style>