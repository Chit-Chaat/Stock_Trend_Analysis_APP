<template>
  <el-container>
    <el-header>
      <el-select v-model="stock_ticker" filterable placeholder="Choose a Stock" style="width: 300px;">
        <el-option v-for="item in ticker_options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-date-picker style="margin-left: 20px; margin-right: 20px; " v-model="start_date" align="right" type="date"
        placeholder="Specify Date" :picker-options="pickerOptions">
      </el-date-picker>
      <el-button type="success" icon="el-icon-upload" style="width: 180px;">Load History</el-button>
      <el-button type="primary" style="margin-left:20px; width: 180px;">Predict Future<i class="el-icon-search el-icon--right"></i></el-button>
    </el-header>
    <el-main id="index_content">
      Echart Panel
    </el-main>
  </el-container>
</template>

<script>
  export default {
    data() {
      return {
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
        stock_ticker: '',
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
            text: 'Two year ago',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 365 * 2);
              picker.$emit('pick', date);
            }
          }

          ]
        },
        start_date: '',
      }
    }
  }
</script>

<style scoped>
  #index_content {
    background-color: #355e86;
    line-height: 380px;
  }

  .el-header {
    color: #333;
    text-align: center;
    line-height: 60px;
  }


</style>