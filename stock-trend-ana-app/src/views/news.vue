<template>
  <el-container id="news_container">
    <el-header>
      <el-select v-model="stock_ticker" filterable placeholder="Choose a Stock" style="width: 300px;">
        <el-option v-for="item in ticker_options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-button type="success" style="margin-left:20px; width: 180px;">Do Filter<i
          class="el-icon-s-operation el-icon--right"></i></el-button>
    </el-header>
    <el-main id="news_content">
      <el-timeline>
        <el-timeline-item v-for="(activity, index) in activities" :key="index" :icon="activity.icon"
          :type="activity.type" :color="activity.color" size="large" :timestamp="activity.timestamp">
          <el-link :href="activity.url" :underline="false" target="_self">{{activity.content}}</el-link>
          <div>
            <el-tag v-for="tag in activity.tags" :key="tag.name" :type="tag.type">
              {{tag.name}}
            </el-tag>
          </div>
        </el-timeline-item>
      </el-timeline>
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
        activities: [{
          content: '3 Stocks to Buy and Hold for the Next 10 Years',
          timestamp: '2021-04-12 20:46',
          type: 'primary',
          icon: 'el-icon-more',
          url: "http://www.baidu.com",
          tags: [
            { name: 'Tag1', type: '' },
            { name: 'Tag2', type: 'success' },
            { name: 'Tag2Tag3', type: 'info' },
            { name: 'Tag4', type: 'warning' },
            { name: 'Tag5Tag2', type: 'danger' }
          ]
        }, {
          content: 'Amazon May Do More Than Make You Rich, It Could Literally Save Your Life One Day',
          timestamp: '2021-04-03 20:46',
          color: '#355e86'
        }, {
          content: 'Cathie Wood Is Buying Teladoc. Should You?',
          timestamp: '2021-04-03 20:46',
          size: 'large'
        }, {
          content: 'Ballot review enters second day in landmark Amazon union election',
          timestamp: '2021-04-03 20:46'
        }, {
          content: '3 Robinhood Stocks That Are Great Buys',
          timestamp: '2021-04-03 20:46'
        }, {
          content: '3 Robinhood Stocks That Are Great Buys',
          timestamp: '2021-04-03 20:46'
        }, {
          content: '3 Robinhood Stocks That Are Great Buys',
          timestamp: '2021-04-03 20:46'
        }, {
          content: '3 Robinhood Stocks That Are Great Buys',
          timestamp: '2021-04-03 20:46'
        }
        ],
      }
    }
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
</style>