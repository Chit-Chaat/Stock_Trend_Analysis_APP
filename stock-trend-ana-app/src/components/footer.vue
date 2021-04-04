<template>
  <div>
    <div id="sider_footer"></div>
    <div id="actual_footer">
      <el-row :gutter="20" style="padding-left: 62px;">
        <el-col :span="6">
          <el-tooltip effect="light" placement="top">
            <div slot="content">多行信息<br/>第二行信息</div>
            <el-card shadow="hover" class="grid-content bg-purple-light">
              总是显示
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="4">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              总是显示
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="4">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              总是显示
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="9">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              总是显示
            </el-card>
          </el-tooltip>
        </el-col>
      </el-row>
    </div>
    <div id="footer_footer">

    </div>
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
    border-radius: 0 0 20px 0;
  }

  #actual_footer {
    background-color: #ecf0f4;
    display: inline;
    height: 150px;
    width: -webkit-calc(100% - 200px);
    padding: 0;
    float: right;
  }

  #footer_footer {
    background-color: #ecf0f4;
    float: left;
    line-height: 30px;
    width: 100%;
    height: 30px;
  }

  .el-row {
    margin: 0 !important;
  }

  .el-col {
    border-radius: 4px;
  }

  .bg-purple-light {
    background: #ffffff;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    height: 140px;
    margin-top: 6px;
    box-shadow: 2px 2px 10px #cecece;
  }
</style>