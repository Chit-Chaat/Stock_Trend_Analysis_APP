<template>
  <el-container>
    <el-header>Header</el-header>
    <el-main>Main</el-main>
    <el-footer>Footer</el-footer>
  </el-container>

</template>
<style>
  .el-header{
    width: 100%;
    height: 100px !important;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 100px;
  }

  .el-footer {
    width: 100%;
    height: 200px !important;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 300px;
    height: 400px;
  }

  body>.el-container {
    margin-bottom: 40px;
  }
</style>