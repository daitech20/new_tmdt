<template>
	<a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
			<a-layout>
				<a-page-header
				style="border: 1px solid rgb(235, 237, 240)"
				title="Product"
				sub-title="Danh mục product" />
				<a-layout-content style="padding: 0 50px">
					<router-link :to="{ name: 'product.create' }" >
						<a-button class="editable-add-btn" style="margin-bottom: 8px">Add</a-button>
					</router-link>
					<a-table :columns="columns" :data-source="data" :scroll="{ x: 1000, y: 500 }">
						<template #bodyCell="{ column, record }">
						<template v-if="column.dataIndex === 'name'">
							<router-link :to="{ name: 'product.detail', params: { product_id: record.id }}" >
								<a type="primary" size="small"> {{ record.name }} </a>
							</router-link>   
						</template>
                        <template v-if="column.dataIndex === 'image'">
                            <a-image
                                :width="50"
                                :src="record.image"
                            />
                        </template>
                        <template v-if="column.dataIndex === 'category'">
                            <a>{{ record.category.name }}</a>
                        </template>
                        <template v-if="column.dataIndex === 'brand'">
                            <a>{{ record.brand.name }}</a>
                        </template>
                        <template v-if="column.dataIndex === 'keyword'">
							<div v-for="k in record.keyword">
                                <a>{{ k.name }}</a>
                            </div>
						</template>
						<template v-if="column.dataIndex === 'is_active'">
							<a v-if="record.is_active" type="primary" size="small"> True </a>
                            <a v-else type="primary" size="small"> False </a>
						</template>
						<template v-if="column.dataIndex === 'option'">
							<a-button type="primary" danger size="small" @click="showModalDelete(record.id, record.name)">Delete</a-button>
						</template>
						</template>
					</a-table>
				</a-layout-content>
				<a-modal v-model:visible="visible" title="Delete" @ok="handleDelete()">
				<p>
					Do you want to delete {{ this.product_name_del }}?
				</p>
				</a-modal>
			</a-layout>
			<DashBoardFooter/>
		</a-layout>
	</a-layout>
</template>

<script>

import BaseRequest from '../../core/BaseRequest.js';
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';
import { notification } from 'ant-design-vue';
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'

export default({
	data() {
		return {
			columns: [],
			products: [],
			errors: {},
			data: [],
			visible: false,
            product_id_del: null,
            product_name_del: null,
		}
	},
	mounted() {
		this.getData()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
	components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter
    },
	methods: {
		getData: function() {
			this.columns = [
                {
				title: 'Id',
				dataIndex: 'id',
				key: 'id'
				},
                {
				title: 'Image',
				dataIndex: 'image',
				key: 'image'
				},
				{
				title: 'Tên product',
				dataIndex: 'name',
				key: 'name'
				},
				{
				title: 'Mô tả',
				dataIndex: 'description',
				key: 'description'
				},
                {
				title: 'Giá',
				dataIndex: 'price',
				key: 'price'
				},
                {
				title: 'Category',
				dataIndex: 'category',
				key: 'category'
				},
                {
				title: 'Brand',
				dataIndex: 'brand',
				key: 'brand'
				},
                {
				title: 'keyword',
				dataIndex: 'keyword',
				key: 'keyword'
				},
                {
				title: 'Trạng thái',
				dataIndex: 'is_active',
				key: 'is_active'
				},
                {
				title: 'Lựa chọn',
				dataIndex: 'option',
				key: 'option'
				},
			];

			this.getProducts()
		},

		getProducts: function() {
			this.data = []
			BaseRequest.get('products/product/list')
			.then(response => {
				this.products = response.data
				for (const num in this.products) {
					this.data.push({
					    name: this.products[num].name,
						description: this.products[num].description,
                        id: this.products[num].id,
                        is_active: this.products[num].is_active,
                        keyword: this.products[num].keyword,
                        price: this.products[num].price,
                        brand: this.products[num].brand,
                        category: this.products[num].category,
                        image: this.products[num].image
					})
				}
                console.log(this.products)
			})
			.catch(error=> {
				this.errors = error.response.data
			});
		},
        showModalDelete: function(id, name) {
			this.product_id_del = id
			this.product_name_del = name
			this.visible = true
		},

        handleDelete: function() {
			this.visible = false
			BaseRequest.delete('products/product/update/' + this.product_id_del)
				.then(response => {
					this.errors = {}
					this.delSuccessNotification()
                    for (let key=0; key<this.data.length; key++) {
						if (this.data[key].id === this.product_id_del) {
                            this.data.splice(key, 1)
                            break
						}
					}
					this.$router.push({ name: 'product.list'});
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log(this.errors)
				});
		},
        delSuccessNotification: function() {
			notification['success']({
				message: 'Delete successfully!',
				description:
				'Product was deleted! ',
			});
		}
	}
})
</script>