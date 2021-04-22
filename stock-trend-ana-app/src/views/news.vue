<template>
  <el-container id="news_container">
    <el-header>
      <el-select v-model="stock_ticker" filterable placeholder="Choose a Stock" style="width: 300px;">
        <i slot="prefix" class="el-input__icon el-icon-search"></i>
        <el-option v-for="item in ticker_options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-button type="success" style="margin-left:20px; width: 180px;" @click="crawl_new">Do Filter<i
          class="el-icon-s-operation el-icon--right"></i></el-button>
    </el-header>
    <el-main id="news_content" v-loading.fullscreen.lock="loading">
      <div id="news_cover" v-show="cover_show">Failed to get News Data.</div>
      <div id="news_cover2" v-show="cover_show">Please contact the admin team.</div>
      <el-timeline>
        <el-timeline-item v-for="(activity, index) in activities" :key="index"
          :type="activity.type" :color="activity.color" size="large" :timestamp="activity.timestamp">
          <el-alert :title="activity.content" :type="activity.type" :description="wrapper(activity.url)"
            close-text="Read more" @close="go_that_url(activity.url)">
          </el-alert>
        </el-timeline-item>
      </el-timeline>
    </el-main>
  </el-container>
</template>

<script>
  import axios from "axios"
  import { bus } from '../main'
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
        stock_ticker: 'AMZN',
        crawlNewApiPrefix: '/analysis/news/latest/',
        activities: [],
        loading: true,
        cover_show: false,
      }
    },
    mounted() {
      this.cover_show = false
      this.crawl_new()
      this.stock_ticker = ''
    },
    watch: {
      stock_ticker() {
        bus.$emit("selectedStockTicker", this.stock_ticker)
      }
    },
    methods: {
      wrapper(text) {
        return "Came from " + text
      },
      isNull(str) {
        return !str && str !== 0 && typeof str !== "boolean" ? true : false;
      },
      go_that_url(url_str) {
        window.open(url_str, '_blank');
      },
      crawl_new() {
        this.loading = true
        if (this.isNull(this.stock_ticker)) {
          this.$options.methods.sendTips.bind(this)("You can check other stock news by clicking filter.");
        } else {
          axios({
            method: "GET",
            url: this.$hostname + this.crawlNewApiPrefix + this.stock_ticker
          }).then(
            result => {
              if (result.data != null) {
                if (result.data.code == 200) {
                  this.activities = result.data.data;
                  this.$options.methods.sendSuccessMsg.bind(this)("Crawl Real Time News data successfully.");
                  this.loading = false
                } else {
                  this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
                }
              }
            },
            error => {
              this.$options.methods.sendErrorMsg.bind(this)(
                "Something wrong with crawling Stock Market News Data."
              );
              this.loading = false
              this.cover_show = true
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
  #news_container {
    position: relative;
    height: 480px;
  }

  #news_content {
    overflow: auto;
  }


  #news_content::-webkit-scrollbar {
    width: 0;
  }


  .el-header {
    color: #333;
    line-height: 60px;
  }

  .el-timeline {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
  }

  .el-timeline-item {
    position: relative;
    line-height: 20px;
    width: auto;
    text-align: left;
    font-family: "Microsoft YaHei";
  }

  .el-timeline-item__content {
    color: #303133;
  }
  #news_cover {
    float: left;
    padding-left: 22%;
    margin-top: 5%;
    font-family: Microsoft YaHei;
    color: #C0C4CC;
    font-size: 60px;
    font-weight: 500;
  }
  #news_cover2 {
    float: left;
    padding-left: 30%;
    margin-top: 0%;
    font-family: Microsoft YaHei;
    color: #C0C4CC;
    font-size: 30px;
    font-weight: 500;
  }
</style>