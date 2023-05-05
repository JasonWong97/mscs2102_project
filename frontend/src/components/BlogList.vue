<!--<template>-->
<!--  <div class="BlogList" v-loading="loading">-->
<!--    <el-card class="card-content" v-for="dat in blogList" :key="dat.title">-->
<!--      <div slot="header" class="card-header-text">-->
<!--        <span style="font-size: 18px; font-weight: bolder">{{ dat.title }}</span>-->
<!--        <div style="float: right; font-size: 5px"> {{ dat.time }} &#45;&#45; {{ dat.user }} </div>-->
<!--      </div>-->
<!--      <div>-->
<!--        <span style="font-size: 10px">{{ dat.content }}</span>-->
<!--      </div>-->
<!--    </el-card>-->
<!--  </div>-->
<!--</template>-->
<template>
  <el-row :gutter="20">
    <el-col :span="6">
<!--      <el-autocomplete-->
<!--        v-model="state"-->
<!--        :fetch-suggestions="querySearchAsync"-->
<!--        placeholder="Search Currency"-->
<!--        @select="handleSelect"-->
<!--      ></el-autocomplete>-->
<!--      <el-row>-->
<!--        <el-button type="primary">Add to my list</el-button>-->
<!--      </el-row>-->

    </el-col>
    <el-col :offset="6" :span="18">
      <div class="MyCrypto" v-loading="loading">
        <el-table
          :data="tableData"
          style="width: 100%"
          max-height="1000">
          <el-table-column
            fixed
            prop="type"
            label="Currency Type"
            width="150">
          </el-table-column>
          <el-table-column
            prop="price"
            label="Real Time Price($)"
            width="300">
          </el-table-column>
<!--          <el-table-column-->
<!--            prop="province"-->
<!--            label="History High"-->
<!--            width="120">-->
<!--          </el-table-column>-->
<!--          <el-table-column-->
<!--            prop="city"-->
<!--            label="History Low"-->
<!--            width="120">-->
<!--          </el-table-column>-->
<!--          <el-table-column-->
<!--            prop="address"-->
<!--            label="地址"-->
<!--            width="300">-->
<!--          </el-table-column>-->
<!--          <el-table-column-->
<!--            prop="zip"-->
<!--            label="邮编"-->
<!--            width="120">-->
<!--          </el-table-column>-->
<!--          <el-table-column-->
<!--            fixed="right"-->
<!--            label="operation"-->
<!--            width="300">-->
<!--            &lt;!&ndash;            <template slot-scope="scope">&ndash;&gt;-->
<!--            &lt;!&ndash;              <el-button&ndash;&gt;-->
<!--            &lt;!&ndash;                @click.native.prevent="deleteRow(scope.$index, tableData)"&ndash;&gt;-->
<!--            &lt;!&ndash;                type="text"&ndash;&gt;-->
<!--            &lt;!&ndash;                size="small">&ndash;&gt;-->
<!--            &lt;!&ndash;                移除&ndash;&gt;-->
<!--            &lt;!&ndash;              </el-button>&ndash;&gt;-->
<!--            &lt;!&ndash;            </template>&ndash;&gt;-->
<!--            <template slot-scope="scope">-->
<!--              <el-button @click="handleClick(scope.row)" type="text" size="small">go to candle</el-button>-->
<!--              <el-button type="text" size="small">delete</el-button>-->
<!--            </template>-->
<!--          </el-table-column>-->
        </el-table>
      </div>
    </el-col>
  </el-row>

</template>
<script>
export default {
  name: 'BlogList',
  data () {
    return {
      blogList: null,
      loading: true,
      tempdata:[],
      tableData: [{
        type: 'BTC',
        price: 0,
        province: '$52330',
        city: '$0.0001',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, {
        type: 'ETH',
        price: 0,
        province: '$52330',
        city: '$0.0001',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, {
        type: 'BNB',
        price: 0,
        province: '$52330',
        city: '$0.0001',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, {
        type: 'ADA',
        price: 0,
        province: '$52330',
        city: '$0.0001',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, {
        type: 'USDT',
        price: 0,
        province: '$52330',
        city: '$0.0001',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, ]

    }
  },
  created () {
    this.$http.get('apis/get_info?blog_list=true&aa=60&kk=6')
      .then(response => {
        this.blogList = response.data.data
        this.loading = false
      }, error => {
        console.log('获取bloglist出错了.')
      })
    this.$http.get('apis/crypto_list_data')
      .then(response => {
        // this.blogList = response.data.data
        // this.loading = false
        console.log('get apis/crypto_list_data')
      }, error => {
        console.log('获取bloglist出错了.')
      })
    this.get_realtime_price()
  },
  methods: {
    deleteRow (index, rows) {
      rows.splice(index, 1)
    },

    get_realtime_price () {
      this.$http.get('apis/get_realtime_price')
        .then(response => {
          this.tempdata=JSON.parse(response.data.crypto_price_data)
          this.tableData[0].price = this.tempdata["BTC"]
          this.tableData[1].price = this.tempdata["ETH"]
          this.tableData[2].price = this.tempdata["BNB"]
          this.tableData[3].price = this.tempdata["ADA"]
          this.tableData[4].price = this.tempdata["USDT"]
          // console.log(this.BTC)
          console.log(response)
          console.log(response.data.crypto_price_data)
          console.log(this.tempdata["BTC"])
        })
    },
  },
  mounted () {
    this.timer = setInterval(this.get_realtime_price, 50000)
  },
  beforeDestroy () {
    clearInterval(this.timer)
  }
}
</script>


<style scoped>
.card-content {
  min-width: 250px;
  max-width: 550px;
  margin: auto;
  margin-bottom: 20px;
}

.card-header-text {
  height: 8px;
}

.card-header-text span {
  font-size: 9px;
  color: #909399;
}

</style>
