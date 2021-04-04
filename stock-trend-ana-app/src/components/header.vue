<template>
  <div>
    <div id="title">

    </div>
    <div id="about">
      <span>Team Oracle (G5):</span>
      <el-divider direction="vertical"></el-divider>
      <el-avatar shape="square" :size="12" :src="squareUrl"></el-avatar>
      <span> Linle Jiang</span>
      <el-divider direction="vertical"></el-divider>
      <el-avatar shape="square" :size="12" :src="squareUrl"></el-avatar>
      <span> Jiaxin Liang</span>
      <el-divider direction="vertical"></el-divider>
      <el-avatar shape="square" :size="12" :src="squareUrl"></el-avatar>
      <span> Bo Yang</span>
    </div>
    <el-divider></el-divider>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        squareUrl: "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
      }
    }
  }
</script>

<style scoped>
  #title{
    height: 50px;
  }
  #about{
    font-family: Microsoft YaHei;
    font-size: 12px;
    float: right;
    line-height: 30px;
  }
</style>