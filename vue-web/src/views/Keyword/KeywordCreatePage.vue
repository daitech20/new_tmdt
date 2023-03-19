<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Thêm từ khóa"
                sub-title="This is a subtitle of create keyword page" />
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
            keyword: {
                name: '',
                description: '',
            },
            errors: {},
        }
    },
    mounted() {

    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, 
    },

    methods: {
        onFinish: function() {
            BaseRequest.post('products/keyword/create', {
                name: this.keyword.name,
                description: this.keyword.description,
            })
            .then(response => {
                    this.errors = {}
                    this.createSuccessNotification()
                    this.$router.push({ name: 'keyword.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                if (this.errors.name) {
                    this.errorsNotification("Thêm keyword thất bại", this.errors.name[0])
                }
                else {
                    this.errorsNotification("Thêm keyword thất bại", "")
                }
                console.log(this.errors)
            });
            
        },
        createSuccessNotification: function() {
            notification['success']({
                message: 'Create successfully!',
                description:
                'Keyword was create! ',
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