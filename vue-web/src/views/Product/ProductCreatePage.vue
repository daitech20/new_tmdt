<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Thêm product"
                sub-title="This is a subtitle of create product page" />
                <a-layout-content style="padding: 0 50px">
                    <a-form
                        :model="product"
                        name="nest-messages"
                        :label-col="{ span: 4 }"
                        :wrapper-col="{ span: 16 }"
                        @finish="onFinish"
                    >
                        <a-form-item
                            :name="['name']"
                            label="Tên product"
                            :rules="[{ required: true, message: 'Vui lòng nhập tên product!' }]"
                        >
                            <a-input v-model:value="product.name" />
                        </a-form-item>
                        
                        <a-form-item
                            :name="['description']"
                            label="Mô tả"
                            :rules="[{ required: true, message: 'Vui lòng nhập mô tả!' }]"
                        >
                            <a-input v-model:value="product.description" />
                        </a-form-item>
                        
                        <a-form-item 
                            :name="['image']"
                            label="Hình ảnh"
                        >
                            <img :src="previewImage" class="uploading-image" />
                            <input type="file" accept="image/jpg" @change=uploadImage>
                        </a-form-item>

                        <a-form-item
                            :name="['price']"
                            label="Giá"
                            :rules="[{ required: true, message: 'Vui lòng nhập giá tiền!' }]"
                        >
                            <a-input v-model:value="product.price" />
                        </a-form-item>

                        <a-form-item
                            :name="['category']"
                            label="Category"
                        >
                            <a-select
                                v-model:value="value_category"
                                label-in-value
                                style="width: 120px"
                                :options="options_category"
                            ></a-select>
                        </a-form-item>

                        <a-form-item
                            :name="['brand']"
                            label="Brand"
                        >
                            <a-select
                                v-model:value="value_brand"
                                label-in-value
                                style="width: 120px"
                                :options="options_brand"
                            ></a-select>
                        </a-form-item>

                        <a-form-item
                            :name="['keyword']"
                            label="Keyword"
                        >
                            <a-select
                                v-model:value="value"
                                mode="tags"
                                style="width: 100%"
                                placeholder="Tags Mode"
                                :options="options"
                                @change="handleChange"
                            ></a-select>
                        </a-form-item>

                        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                            <a-button type="primary" html-type="submit" >Thêm</a-button>
                        </a-form-item>
                    </a-form>
                </a-layout-content>
            </a-layout>
            <DashBoardFooter/>
		</a-layout>
	</a-layout>
</template>

<script lang="ts">
import BaseRequest from '../../core/BaseRequest.js'
import { notification } from 'ant-design-vue';
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'
import {UploadOutlined} from '@ant-design/icons-vue'

export default({
    data() {
        return {
            product: {
                name: '',
                description: '',
                price: 0,
                image: null,
            },
            keywords: [],
            errors: {},
            value: [],
            options: [],
            options_category: [],
            value_category: {},
            options_brand: [],
            value_brand: {},
            categories: {},
            brands: {},
            previewImage: null
        }
    },
    mounted() {
        this.getData()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, UploadOutlined
    },

    methods: {
        uploadImage: function(e) {
            const image = e.target.files[0];
            const reader = new FileReader();
            reader.readAsDataURL(image);
            reader.onload = e =>{
                this.previewImage = e.target.result;
                console.log(this.previewImage);
            };
        },

        handleChange: function(value: string) {
            console.log(`selected ${value}`);
        },

        getData: function() {
            BaseRequest.get('products/keyword/list')
			.then(response => {
				this.keywords = response.data
                for (let k in this.keywords) {
                    this.options.push({
                        value: this.keywords[k].id,
                        label: this.keywords[k].name
                    })
                }
			})
			.catch(error=> {
				this.errors = error.response.data
			});

            BaseRequest.get('products/category/list')
			.then(response => {
				this.categories = response.data
                for (let ct in this.categories) {
                    this.options_category.push(
                        {
                            value: this.categories[ct].id,
                            label: this.categories[ct].name
                        }
                    )
                }
                this.value_category = this.options_category[0]
			})
			.catch(error=> {
				this.errors = error.response.data
			});

            BaseRequest.get('products/brand/list')
			.then(response => {
				this.brands = response.data
                for (let br in this.brands) {
                    this.options_brand.push(
                        {
                            value: this.brands[br].id,
                            label: this.brands[br].name
                        }
                    )
                }
                this.value_brand = this.options_brand[0]
			})
			.catch(error=> {
				this.errors = error.response.data
			});
        },

        onFinish: function() {
            BaseRequest.post('products/product/create', {
                name: this.product.name,
                description: this.product.description,
                keyword: this.value,
                category: this.value_category.value,
                brand: this.value_brand.value,
                price: this.product.price,
                image: this.previewImage
            })
            .then(response => {
                    this.errors = {}
                    this.createSuccessNotification()
                    this.$router.push({ name: 'product.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                if (this.errors.name) {
                    this.errorsNotification("Thêm product thất bại", "name:" + this.errors.name[0])
                }
                else if (this.errors.image) {
                    this.errorsNotification("Thêm product thất bại", "image:" + this.errors.image[0])
                }
                else if (this.errors.price) {
                    this.errorsNotification("Thêm product thất bại", "price:" + this.errors.price[0])
                }
                else if (this.errors.brand) {
                    this.errorsNotification("Thêm product thất bại", "brand:" + this.errors.brand[0])
                }
                else if (this.errors.category) {
                    this.errorsNotification("Thêm product thất bại", "category:" + this.errors.category[0])
                }
                else {
                    this.errorsNotification("Thêm product thất bại", "")
                }
                console.log(this.errors)
            });
            
        },
        createSuccessNotification: function() {
            notification['success']({
                message: 'Create successfully!',
                description:
                'Product was create! ',
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        },
    },
})
</script>

<style>
.uploading-image{
     display:flex;
     max-width: 500px;
   }
</style>