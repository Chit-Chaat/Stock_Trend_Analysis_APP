<template>
  <el-container>
    <el-header>
      <el-select v-model="stock_ticker" filterable placeholder="Choose a Stock" style="width: 300px;">
        <i slot="prefix" class="el-input__icon el-icon-search"></i>
        <el-option v-for="item in ticker_options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-date-picker style="margin-left: 20px; margin-right: 20px; " v-model="start_date" align="right" type="date"
        placeholder="Specify Date" :picker-options="pickerOptions">
      </el-date-picker>
      <el-button type="success" icon="el-icon-download" style="width: 180px;" @click="load_history">Load History
      </el-button>
      <el-button type="primary" style="margin-left:20px; width: 180px;" @click="predict_future">Predict Future<i
          class="el-icon-data-line el-icon--right" ></i></el-button>
    </el-header>
    <el-main id="index_content" v-loading.fullscreen.lock="loading">
      <div id="candle_cover" v-show="cover_show">{{cover_msg}}</div>
      <div id="echartContainer" ref="echartContainer" style="width:100%; height:380px"></div>
    </el-main>
  </el-container>
</template>

<script>
  var echarts = require("echarts");
  import axios from "axios"
  export default {

    data() {
      return {
        renderDataApiPrefix: "/analysis/candle/",
        predictApiPrefix: "/analysis/predict/",
        upColor: '#67C23A',
        downColor: '#F56C6C',
        ticker_options: [{
          value: 'AMZN',
          label: 'AMZN (Amazon)'
        }, {
          value: 'BOTZ',
          label: 'BOTZ (Robotics & AI ETF)'
        }, {
          value: 'GOOG',
          label: 'GOOG (Google)'
        }, {
          value: 'FB',
          label: 'FB (Facebook)'
        }, {
          value: 'AAPL',
          label: 'AAPL (Apple)'
        }, {
          value: 'NFLX',
          label: 'NFLX (Netflix)'
        }, {
          value: 'MSFT',
          label: 'MSFT (Microsoft)'
        }, {
          value: 'XLK',
          label: 'XLK (SPDR Fund)'
        }
        ],
        pickerOptions: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: 'Today',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: 'Yesterday',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: 'A week ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }, {
            text: 'A month ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 31);
              picker.$emit('pick', date);
            }
          }, {
            text: 'A year ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 365);
              picker.$emit('pick', date);
            }
          }, {
            text: '2 year ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 365 * 2);
              picker.$emit('pick', date);
            }
          }, {
            text: '3 year ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 365 * 3);
              picker.$emit('pick', date);
            }
          }

          ]
        },
        start_date: '',
        stock_ticker: '',
        stock_data: {},
        cover_show: true,
        loading: false,
        cover_msg: "",
      }
    },
    mounted() {
      this.cover_msg = "Please Select One Stock"
      this.cover_show = true;
      this.drawCandleChart();
    },
    watch: {
      stock_data(val) {
        this.drawCandleChart();
      }
    },
    methods: {
      isNull(str) {
        return !str && str !== 0 && typeof str !== "boolean" ? true : false;
      },
      drawCandleChart() {
        var orginalData = this.stock_data;
        var option = {
          animation: false,
          legend: {
            bottom: 360,
            left: 'center',
            data: ['Daily Value', 'MA5', 'MA10', 'MA20', 'MA30', 'prediction']
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross'
            },
            borderWidth: 1,
            borderColor: '#E4E7ED',
            padding: 10,
            textStyle: {
              color: '#909399'
            },
            position: function (pos, params, el, elRect, size) {
              var obj = { top: 10 };
              obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
              return obj;
            }
          },
          axisPointer: {
            link: { xAxisIndex: 'all' },
            label: {
              backgroundColor: '#409EFF'
            }
          },
          toolbox: {
            feature: {
              dataZoom: {
                yAxisIndex: false
              },
              brush: {
                type: ['lineX', 'clear']
              }
            }
          },
          brush: {
            xAxisIndex: 'all',
            brushLink: 'all',
            outOfBrush: {
              colorAlpha: 0.3
            }
          },
          visualMap: {
            show: false,
            seriesIndex: 6,
            dimension: 2,
            pieces: [{
              value: 1,
              color: this.downColor
            }, {
              value: -1,
              color: this.upColor
            }]
          },
          grid: [
            {
              // candle chart
              left: "3%",
              right: "3%",
              top: "0",
              height: "75%"
            },
            {
              // volume bar chart
              left: "3%",
              right: "3%",
              top: "80%",
              height: "10%"
            }
          ],
          xAxis: [
            {
              type: "category",
              data: orginalData.categoryData,
              scale: true,
              boundaryGap: false,
              axisLine: {
                onZero: false,
                lineStyle: {
                  color: '#606266'
                }
              },
              splitLine: {
                show: false
              },
              splitNumber: 20,
              min: 'dataMin',
              max: 'dataMax',
              axisPointer: {
                z: 100
              }
            },
            {
              type: 'category',
              gridIndex: 1,
              data: orginalData.categoryData,
              scale: true,
              boundaryGap: false,
              axisLine: { onZero: false },
              axisTick: { show: false },
              splitLine: { show: false },
              axisLabel: { show: false },
              splitNumber: 20,
              min: 'dataMin',
              max: 'dataMax'
            }
          ],
          yAxis: [
            {
              scale: true,
              splitArea: {
                show: true
              },
              axisLine: {
                onZero: false,
                lineStyle: {
                  color: '#606266'
                }
              },
              position: "right"
            },
            {
              gridIndex: 1,
              splitNumber: 3,
              axisTick: { show: false },
              splitLine: { show: false },
              axisLabel: { show: true },
              position: "right"
            }
          ],
          dataZoom: [
            {
              type: "inside",
              start: 100,
              end: 80
            },
            {
              show: true,
              type: "slider",
              y: "90%",
              start: 50,
              end: 100
            },
            {
              show: false,
              xAxisIndex: [0, 1],
              type: "slider",
              start: 20,
              end: 100
            }
          ],
          series: [
            {
              name: "Daily Value",
              type: "candlestick",
              data: orginalData.values,
              itemStyle: {
                color: this.upColor,
                color0: this.downColor,
                borderColor: null,
                borderColor0: null
              },
              tooltip: {
                formatter: function (param) {
                  param = param[0];
                  return [
                    'Date: ' + param.name + '<hr size=1 style="margin: 0 0;">',
                    'Open: ' + param.data[0] + '<br/>',
                    'Close: ' + param.data[1] + '<br/>',
                    'Lowest: ' + param.data[2] + '<br/>',
                    'Highest: ' + param.data[3] + '<br/>'
                  ].join('');
                }
              }
            },
            {
              name: "MA5",
              type: "line",
              data: orginalData.MA5,
              smooth: true,
              lineStyle: {
                normal: {
                  opacity: 0.5
                }
              }
            },
            {
              name: "MA10",
              type: "line",
              data: orginalData.MA10,
              smooth: true,
              lineStyle: {
                normal: {
                  opacity: 0.5
                }
              }
            },
            {
              name: "MA20",
              type: "line",
              data: orginalData.MA20,
              smooth: true,
              lineStyle: {
                normal: {
                  opacity: 0.5
                }
              }
            },
            {
              name: "MA30",
              type: "line",
              data: orginalData.MA30,
              smooth: true,
              lineStyle: {
                normal: {
                  opacity: 0.5
                }
              }
            },
            {
              name: "prediction",
              type: "line",
              data: orginalData.prediction,
              smooth: true,
              lineStyle: {
                normal: {
                  opacity: 0.5
                }
              }
            },
            {
              name: 'Volume',
              type: 'bar',
              xAxisIndex: 1,
              yAxisIndex: 1,
              data: orginalData.volumes
            }
          ]
        };
        var charts = echarts.init(this.$refs.echartContainer);
        charts.setOption(option);
        charts.dispatchAction({
          type: 'brush',
          areas: [
            {
              brushType: 'lineX',
              coordRange: ['2020-7-15', '2020-7-20'],
              xAxisIndex: 0
            }
          ]
        });

      },
      load_history() {
        if (this.isNull(this.start_date) || this.isNull(this.stock_ticker)) {
          this.$options.methods.sendErrorMsg.bind(this)("Please assign Ticker and Data first.");
        } else {
          this.loading = true;
          var start_date_str = this.start_date.toISOString().substring(0, 10)
          axios({
            method: "GET",
            url: this.$hostname + this.renderDataApiPrefix + start_date_str + "/" + this.stock_ticker
          }).then(
            result => {
              if (result.data != null) {
                if (result.data.code == 200) {
                  this.stock_data = result.data.data;
                  this.$options.methods.sendSuccessMsg.bind(this)("Load historical data successfully.");
                  this.cover_show = false;
                  this.loading = false;
                } else {
                  this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
                }
              }
            },
            error => {
              this.$options.methods.sendErrorMsg.bind(this)(
                "Something wrong with getting Stock Historical Data."
              );
              this.loading = false;
              this.cover_show = true;
              this.cover_msg = "Failed to load history data."
            }
          );
        }
      },
      predict_future(){
        if (this.isNull(this.start_date) || this.isNull(this.stock_ticker)) {
          this.$options.methods.sendErrorMsg.bind(this)("Please assign Ticker and Data first.");
        } else {
          this.loading = true;
          axios({
            method: "GET",
            url: this.$hostname + this.predictApiPrefix + this.stock_ticker
          }).then(
            result => {
              if (result.data != null) {
                if (result.data.code == 200) {
                  this.stock_data = result.data.data;
                  this.$options.methods.sendSuccessMsg.bind(this)("Load predict future stock value successfully.");
                  this.cover_show = false;
                  this.loading = false;
                } else {
                  this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
                }
              }
            },
            error => {
              this.$options.methods.sendErrorMsg.bind(this)(
                "Something wrong with getting Future Value Data."
              );
              this.loading = false;
              this.cover_show = true;
              this.cover_msg = "Failed to make prediction."
            }
          );
        }
      },
      sendTips(msg) {
        const h = this.$createElement;
        this.$notify.success({
          title: 'Success',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendAlert(msg) {
        const h = this.$createElement;
        this.$notify.warning({
          title: 'Warning',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendSuccessMsg(msg) {
        this.$message.success({
          type: 'Success',
          message: msg
        });
      },
      sendErrorMsg(msg) {
        this.$message.warning({
          type: 'Warning',
          message: msg
        });
      },

    },
  }
</script>

<style scoped>
  #candle_cover {
    float: left;
    padding-left: 22%;
    margin-top: -3%;
    font-family: Microsoft YaHei;
    color: #C0C4CC;
    font-size: 60px;
    font-weight: 500;
  }

  #index_content {
    line-height: 380px;
  }

  .el-header {
    color: #333;
    text-align: center;
    line-height: 60px;
  }
</style>