<template>
  <el-container>
    <el-header>
      <el-select v-model="value" filterable placeholder="请选择">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <el-date-picker v-model="value2" align="right" type="date" placeholder="选择日期" :picker-options="pickerOptions">
      </el-date-picker>
      <el-button type="success" icon="el-icon-upload">Load History</el-button>
      <el-button type="primary">Predict Future<i class="el-icon-search el-icon--right"></i></el-button>
    </el-header>
    <el-main>Main</el-main>
  </el-container>
</template>

<script>
  export default {
    data() {
      return {
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value: '',
        pickerOptions: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        value2: '',
      }
    }
  }
</script>

<style scoped>
  .el-header {
    background-color: #3572c2;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  
  .el-main {
    background-color: #355e86;
    color: #333;
    text-align: center;
    line-height: 0px !important;
  }