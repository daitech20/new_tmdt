<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Thêm brand"
                sub-title="This is a subtitle of create brand page" />
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

export default({
    data() {
        return {
            brand: {
                name: '',
                description: '',
            },
            keywords: [],
            errors: {},
            value: [],
            options: []
        }
    },
    mounted() {
        this.getKeywords()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, 
    },

    methods: {
        handleChange: function(value: string) {
            console.log(`selected ${value}`);
        },

        getKeywords: function() {
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
            BaseRequest.post('products/brand/create', {
                name: this.brand.name,
                description: this.brand.description,
                keyword: this.value
            })
            .then(response => {
                    this.errors = {}
                    this.createSuccessNotification()
                    this.$router.push({ name: 'brand.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                if (this.errors.name) {
                    this.errorsNotification("Thêm brand thất bại", this.errors.name[0])
                }
                else {
                    this.errorsNotification("Thêm brand thất bại", "")
                }
                console.log(this.errors)
            });
            
        },
        createSuccessNotification: function() {
            notification['success']({
                message: 'Create successfully!',
                description:
                'Brand was create! ',
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        },
    }
})
</script>