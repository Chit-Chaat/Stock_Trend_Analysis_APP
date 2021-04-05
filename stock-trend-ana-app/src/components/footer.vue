<template>
  <div>
    <div id="sider_footer"></div>
    <div id="actual_footer">
      <el-row :gutter="20" style="padding-left: 62px; padding-top: 10px;">
        <el-col :span="6">
          <el-tooltip effect="light" placement="top">
            <div slot="content">多行信息<br />第二行信息</div>
            <el-card shadow="hover" class="grid-content bg-purple-light">
              <div class="clearfix"> Stock Market Emotion </div>
              <g2-radar :is-show-area="true" 
              style="width: 200px; height: 200px; margin: 0;"
              :show-legend="true" :axis-name="{a:'companya',b:'companyb',c:'companyc'}"
                :data="[{item: 'Design',a: 70,b: 30,c: 11},
   {item: 'Development',a: 60,b: 70,c: 11},
   {item: 'Marketing',a: 50,b: 60,c: 11},
   {item: 'Users',a: 40,b: 50,c: 11},
   {item: 'Test',a: 60,b: 70,c: 11}]">
              </g2-radar>
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="4">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              <div class="clearfix"> Nasdaq Index </div>
              <g2-sparkline style="width: 150px; height: 60px; margin: 0; padding-top: 10px;"
                :axis-name="{name: 'Date', value: 'value'}" :data="COMP_val_obj.values" :color="'#909399'"
                :is-percent="false" :type="'line'">
              </g2-sparkline>
              <div class="numeric-content" :style="{'color':up_or_down1}">
                <el-row :gutter="0">
                  <el-col :span="11">
                    <div id="lastest">
                      {{COMP_val_obj.lastestVal}}
                    </div>
                  </el-col>
                  <el-col :span="13">
                    <div>
                      <div id="amount">
                        {{COMP_val_obj.change}}
                      </div>
                      <div id="percent">
                        ({{ COMP_val_obj.percentChange}}%)
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </div>
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="4">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              <div class="clearfix"> S&P500 Index </div>
              <g2-sparkline style="width: 150px; height: 60px; margin: 0; padding-top: 10px;"
                :axis-name="{name: 'Date', value: 'value'}" :data="SP500_val_obj.values" :color="'#909399'"
                :is-percent="false" :type="'line'">
              </g2-sparkline>
              <div class="numeric-content" :style="{'color':up_or_down2}">
                <el-row :gutter="0">
                  <el-col :span="11">
                    <div id="lastest">
                      {{SP500_val_obj.lastestVal}}
                    </div>
                  </el-col>
                  <el-col :span="13">
                    <div>
                      <div id="amount">
                        {{SP500_val_obj.change}}
                      </div>
                      <div id="percent">
                        ({{SP500_val_obj.percentChange}}%)
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </div>
            </el-card>
          </el-tooltip>
        </el-col>
        <el-col :span="9">
          <el-tooltip effect="light" content="Top Left 提示文字" placement="top">
            <el-card shadow="hover" class="grid-content bg-purple-light">
              <div class="clearfix"> Stock Market Emotion </div>
            </el-card>
          </el-tooltip>
        </el-col>
      </el-row>
    </div>
    <div id="footer_footer">

    </div>
  </div>
</template>

<script>
  export default {

    data() {
      return {
        upColor: '#67C23A',
        downColor: '#F56C6C',
        COMP_Real_API: "https://finance.api.seekingalpha.com/v2/real-time-prices?symbols=COMP",
        SP500_Real_API: "https://finance.api.seekingalpha.com/v2/real-time-prices?symbols=SP500",
        COMP_val_obj: {
          values: [{ name: 1, value: 86085 }, { name: 2, value: 87085 }, { name: 3, value: 80085 },
          { name: 4, value: 86185 }, { name: 5, value: 87015 }, { name: 6, value: 81085 },
          { name: 7, value: 86285 }, { name: 8, value: 80085 }, { name: 9, value: 81085 },
          { name: 10, value: 86585 }, { name: 11, value: 83085 }, { name: 12, value: 80015 },
          { name: 13, value: 86585 }, { name: 15, value: 83085 }, { name: 15, value: 80015 }],
          percentChange: 1.76,
          change: 47.68,
          lastestVal: 4068.78,

        },
        SP500_val_obj: {
          values: [{ name: 1, value: 86085 }, { name: 2, value: 87085 }, { name: 3, value: 80085 },
          { name: 4, value: 86185 }, { name: 5, value: 87015 }, { name: 6, value: 81085 },
          { name: 7, value: 86285 }, { name: 8, value: 80085 }, { name: 9, value: 81085 },
          { name: 10, value: 86585 }, { name: 11, value: 83085 }, { name: 12, value: 80015 },
          { name: 13, value: 86585 }, { name: 15, value: 83085 }, { name: 15, value: 80015 }],
          percentChange: -1.76,
          change: -47.68,
          lastestVal: 4068.78,

        }
      }
    },
    computed: {
      up_or_down1: function () {
        return this.COMP_val_obj.change > 0 ? this.upColor : this.downColor
      },
      up_or_down2: function () {
        return this.SP500_val_obj.change > 0 ? this.upColor : this.downColor
      }
    }
  }
</script>

<style scoped>
  #sider_footer {
    background-color: #409EFF;
    width: 200px;
    height: 160px;
    padding: 0;
    float: left;
    display: inline;
    border-radius: 0 0 20px 0;
  }

  #actual_footer {
    background-color: #ecf0f4;
    display: inline;
    height: 160px;
    width: -webkit-calc(100% - 200px);
    padding: 0;
    float: right;
  }

  #footer_footer {
    background-color: #ecf0f4;
    float: left;
    line-height: 30px;
    width: 100%;
    height: 20px;
  }

  .clearfix {
    line-height: 1px;
    font-family: Microsoft YaHei;
    color: #909399;
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
    width: auto;
  }

  .numeric-content {
    height: 40px;
    width: 110%;
    margin-top: 5px;
    font-family: Microsoft YaHei;
    color: #909399;
    line-height: 50px;
  }

  #lastest {}

  #percent {
    display: inline;
    font-size: 11px;
  }

  #amount {
    display: inline;
    font-size: 12px;
  }

  #upClass {
    color: #67C23A;
  }

  #downClass {
    color: #F56C6C;
  }
</style>