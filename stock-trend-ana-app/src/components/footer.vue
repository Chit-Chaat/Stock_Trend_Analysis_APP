<template>
  <div>
    <div id="sider_footer"></div>
    <div id="actual_footer">
      <el-row :gutter="20">
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </div>
    <div id="footer_footer">asdadasd</div>
  </div>
</template>

<style scoped>
  #sider_footer {
    background-color: #409EFF;
    width: 200px;
    height: 150px;
    padding: 0;
    float: left;
    display: inline;
  }
  #actual_footer{
    display: inline;
    height: 150px;
    width: -webkit-calc(100% - 200px);
    padding: 0;
    float: right;
  }

  #footer_footer{
    background-color: rgb(202, 156, 156);
    float: left;
    line-height: 30px;
    width: 100%;
  }

  .el-row {
    margin: 0 !important; 
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    height: 140px;
    margin-top:6px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>