<template>
	<a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
			<a-layout>
				<a-page-header
				style="border: 1px solid rgb(235, 237, 240)"
				title="Brand"
				sub-title="Danh mục brand" />
				<a-layout-content style="padding: 0 50px">
					<router-link :to="{ name: 'brand.create' }" >
						<a-button class="editable-add-btn" style="margin-bottom: 8px">Add</a-button>
					</router-link>
					<a-table :columns="columns" :data-source="data" :scroll="{ x: 1000, y: 500 }">
						<template #bodyCell="{ column, record }">
						<template v-if="column.dataIndex === 'name'">
							<router-link :to="{ name: 'brand.detail', params: { brand_id: record.id }}" >
								<a type="primary" size="small"> {{ record.name }} </a>
							</router-link>   
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
					Do you want to delete {{ this.brand_name_del }}?
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
			brands: [],
			errors: {},
			data: [],
			visible: false,
            brand_id_del: null,
            brnad_name_del: null,
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
				title: 'Tên Brand',
				dataIndex: 'name',
				key: 'name'
				},
				{
				title: 'Mô tả',
				dataIndex: 'description',
				key: 'description'
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

			this.getBrands()
		},

		getBrands: function() {
			this.data = []
			BaseRequest.get('products/brand/list')
			.then(response => {
				this.brands = response.data
				for (const num in this.brands) {
					this.data.push({
					    name: this.brands[num].name,
						description: this.brands[num].description,
                        id: this.brands[num].id,
                        is_active: this.brands[num].is_active,
                        keyword: this.brands[num].keyword
					})
				}
                console.log(this.brands)
			})
			.catch(error=> {
				this.errors = error.response.data
			});
		},
        showModalDelete: function(id, name) {
			this.brand_id_del = id
			this.brand_name_del = name
			this.visible = true
		},

        handleDelete: function() {
			this.visible = false
			BaseRequest.delete('products/brand/update/' + this.brand_id_del)
				.then(response => {
					this.errors = {}
					this.delSuccessNotification()
                    for (let key=0; key<this.data.length; key++) {
						if (this.data[key].id === this.brand_id_del) {
                            this.data.splice(key, 1)
                            break
						}
					}
					this.$router.push({ name: 'brand.list'});
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
				'Brand was deleted! ',
			});
		}
	}
})
</script>