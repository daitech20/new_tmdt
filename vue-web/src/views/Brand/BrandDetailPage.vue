<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Chi tiết brand"
                sub-title="" />
                <a-layout-content style="padding: 0 50px">
                    <a-form
                        :model="brand"
                        name="nest-messages"
                        :label-col="{ span: 4 }"
                        :wrapper-col="{ span: 16 }"
                        @finish="onFinish"
                    >
                        <a-form-item
                            :name="['name']"
                            label="Tên brand"
                            :rules="[{ required: true, message: 'Vui lòng nhập tên brand!' }]"
                        >
                            <a-input v-model:value="brand.name" />
                        </a-form-item>
                        
                        <a-form-item
                            :name="['description']"
                            label="Mô tả"
                            :rules="[{ required: true, message: 'Vui lòng nhập mô tả!' }]"
                        >
                            <a-input v-model:value="brand.description" />
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
                        
                        <a-form-item
                            :name="['is_active']"
                            label="Active"
                        >
                            <a-radio-group v-model:value="brand.is_active" name="radioGroup">
                                <a-radio :value=true>Active</a-radio>
                                <a-radio :value=false>None</a-radio>
                            </a-radio-group>

                        </a-form-item>

                        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                            <a-button type="primary" html-type="submit" >Cập nhật</a-button>
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
import { UploadOutlined } from '@ant-design/icons-vue';
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';

export default({
    data() {
        return {
            brand: {
                name: '',
                description: '',
                is_active: true
            },
            value: [],
            options: [],
            keywords: [],
            errors: {},
        }
    },
    mounted() {
        this.getData()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
        handleChange: function(value: string) {
            console.log(`selected ${value}`);
        },

        getData: function() {
            BaseRequest.get('products/brand/update/' + this.$route.params.brand_id)
			.then(response => {
				this.brand.name = response.data.name
                this.brand.description = response.data.description
                this.brand.is_active = response.data.is_active
                this.value = response.data.keyword
			})
			.catch(error=> {
				this.errors = error.response.data
			});

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
        },
        onFinish: function() {
            BaseRequest.put('products/brand/update/' + this.$route.params.brand_id, {
                name: this.brand.name,
                description: this.brand.description,
                is_active: this.brand.is_active,
                keyword: this.value
            })
            .then(response => {
                    this.errors = {}
                    this.updateSuccessNotification()
                    this.$router.push({ name: 'brand.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                if (this.errors.name) {
                    this.errorsNotification("Update brand thất bại", this.errors.name[0])
                }
                else {
                    this.errorsNotification("Update brand thất bại", "")
                }
                console.log(this.errors)
            });
        },

        updateSuccessNotification: function() {
            notification['success']({
                message: 'Update successfully!',
                description:
                'Brand was updated! ',
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        },
    },
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, UploadOutlined
    },
})
</script>