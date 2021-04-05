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
              <div style="display: inline;">
                <g2-pie :type="'ring'" :axis-name="{name:'type', value:'amount'}"
                  style="width: 150px; height: 150px; margin: 0; padding-top: 10px;" :data="emotion_obj"
                  :useTooltip="false">
                </g2-pie>
              </div>
              <div class="textual-content">
                <div v-for="obj in emotion_obj" :key="obj.name" class="textual-item">
                  <i :class="obj.icon"></i>{{ " " + obj.name + " : " + obj.value +'%' }}
                </div>
              </div>
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
          <el-card shadow="hover" class="grid-content bg-purple-light">
            <div class="clearfix"> Net Price Calculator </div>
            <div class="calculator_form">
              <el-form :inline="true" :model="formInline" id="calculator_form_inline">
                <el-form-item>
                  <el-popover placement="top-start" title="标题" width="200" trigger="hover"
                    content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。">
                    <el-button slot="reference" size="mini" icon="el-icon-info" circle></el-button>
                  </el-popover>
                  &nbsp;
                  <el-input size="mini" placeholder="Cost Price" clearable v-model="formInline.region"
                    style="width: 120px;">
                  </el-input>
                </el-form-item>
                <el-form-item>
                  <el-input-number size="mini" v-model="formInline.amount" style="width: 120px;"></el-input-number>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" size="mini" icon="el-icon-video-play"></el-button>
                  <el-button type="danger" size="mini" icon="el-icon-video-pause"></el-button>
                </el-form-item>
              </el-form>
              <el-form :inline="true" :model="formResult" id="form_result_inline">
                <el-form-item>
                  <div id="net_price_title">Net Price:</div>
                </el-form-item>
                <el-form-item>
                  <div class="price_value" :style="{'color':up_or_down3}">{{'$' + formResult.netValue}}</div>
                </el-form-item>
                <el-form-item>
                  <div id="float_price_title">Floating:</div>
                </el-form-item>
                <el-form-item>
                  <div class="price_value" :style="{'color':up_or_down4}">{{'$' + formResult.floatingValue}}</div>
                </el-form-item>
                <el-form-item>
                  <div class="price_value" :style="{'color':up_or_down5}">{{ "(" +formResult.percentChange + "%)"}}</div>
                </el-form-item>
              </el-form>
            </div>
          </el-card>
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

        },
        emotion_obj: [
          { icon: 'el-icon-cloudy-and-sunny', name: 'positive', value: 2 },
          { icon: 'el-icon-lightning', name: 'negative', value: 1 },
          { icon: 'el-icon-partly-cloudy', name: 'neutral', value: 3 }
        ],
        formInline: {
          amount: 10,
          region: ''
        },
        formResult:{
          netValue: 123123,
          floatingValue: 123123,
          percentChange: 12.12,
          change:131,
        }
      }
    },
    computed: {
      up_or_down1: function () {
        return this.COMP_val_obj.change > 0 ? this.upColor : this.downColor
      },
      up_or_down2: function () {
        return this.SP500_val_obj.change > 0 ? this.upColor : this.downColor
      },
      up_or_down3: function () {
        return this.formResult.netValue > 0 ? this.upColor : this.downColor
      },
      up_or_down4: function () {
        return this.formResult.floatingValue > 0 ? this.upColor : this.downColor
      },
      up_or_down5: function () {
        return this.formResult.percentChange > 0 ? this.upColor : this.downColor
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
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

  .textual-content {
    display: inline;
    width: 110px;
    height: 80px;
    position: absolute;
    left: 240px;
    bottom: 20px;
  }

  .textual-item {
    font-family: Microsoft YaHei;
    color: #909399;
    font-size: 14px;
    line-height: 25px;
  }

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

  .calculator_form {
    height: 100px;
    margin-top: 10px;
  }

  #calculator_form_inline{
    height: 50px;
    margin-top: 20px;
  }

  #form_result_inline{
    height: 50px;
    font-family: Microsoft YaHei;
    color: #909399;
  }
  #form_result_inline > .el-form-item__content{
    font-size: 12px !important;
  }

  .price_value{
    font-size: 16px !important;
    font-weight: 600;
  }
</style>