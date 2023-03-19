<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Chi tiết keyword"
                sub-title="" />
                <a-layout-content style="padding: 0 50px">
                    <a-form
                        :model="keyword"
                        name="nest-messages"
                        :label-col="{ span: 4 }"
                        :wrapper-col="{ span: 16 }"
                        @finish="onFinish"
                    >
                        <a-form-item
                            :name="['name']"
                            label="Tên keyword"
                            :rules="[{ required: true, message: 'Vui lòng nhập tên keyword!' }]"
                        >
                            <a-input v-model:value="keyword.name" />
                        </a-form-item>
                        
                        <a-form-item
                            :name="['description']"
                            label="Mô tả"
                            :rules="[{ required: true, message: 'Vui lòng nhập mô tả!' }]"
                        >
                            <a-input v-model:value="keyword.description" />
                        </a-form-item>
                        
                        <a-form-item
                            :name="['is_active']"
                            label="Active"
                        >
                            <a-radio-group v-model:value="keyword.is_active" name="radioGroup">
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
            keyword: {
                name: '',
                description: '',
                is_active: true
            },
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
        getData: function() {
            BaseRequest.get('products/keyword/update/' + this.$route.params.keyword_id)
			.then(response => {
				this.keyword.name = response.data.name
                this.keyword.description = response.data.description
                this.keyword.is_active = response.data.is_active
			})
			.catch(error=> {
				this.errors = error.response.data
			});
        },
        onFinish: function() {
            BaseRequest.put('products/keyword/update/' + this.$route.params.keyword_id, {
                name: this.keyword.name,
                description: this.keyword.description,
                is_active: this.keyword.is_active
            })
            .then(response => {
                    this.errors = {}
                    this.updateSuccessNotification()
                    this.$router.push({ name: 'keyword.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                if (this.errors.name) {
                    this.errorsNotification("Update keyword thất bại", this.errors.name[0])
                }
                else {
                    this.errorsNotification("Update keyword thất bại", "")
                }
                console.log(this.errors)
            });
        },

        updateSuccessNotification: function() {
            notification['success']({
                message: 'Update successfully!',
                description:
                'Keyword was updated! ',
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
1