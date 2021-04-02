<template>
  <div>
    <div id="myChart" style="width: 600px;height: 400px;"></div>
    <el-button type="success" icon="el-icon-check" circle @click="chart_time_btn()"></el-button>
  </div>
</template>

<script>

  var echarts = require("echarts");
  import axios from "axios"
  export default {
    data() {
      return {
        dataArr: ["1月", "2月", "3月", "4月", "5月", "6月"],
        dataVal: [5, 20, 36, 10, 10, 20]
      }
    },
    mounted() {
      this.drawLine();
    },
    watch: {
      dataVal(val) {
        this.drawLine();
      }
    },
    methods: {
      drawLine() {
        var odataArr = this.dataArr;

        let myChart = echarts.init(document.getElementById('myChart'))
        myChart.setOption({
          title: { text: '在Vue中使用echarts' },
          tooltip: {},
          xAxis: {
            data: odataArr

          },
          yAxis: {},
          series: [{
            name: '销量',
            type: 'line',
            data: this.dataVal
          }]
        });
      },

      chart_time_btn() {//点击事件 更改图表数据

        axios({
          method: "GET",
          url: this.$hostname + "/analysis/test"
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.dataVal = result.data.data;
                this.$options.methods.sendSuccessMsg.bind(this)(result.data.msg);
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with getting Stock Historical Data."
            );
          }
        );
      }
    },
    components: {

    },

  }
</script>