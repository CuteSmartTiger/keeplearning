<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>{{ toolbar.title }}</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form v-model="valid" ref="form" lazy-validation>
                  <v-select
                    prepend-icon="home"
                    :items="tenants"
                    v-model="tenant"
                    label="Tenant"
                    :rules="tenantRules"
                    single-line
                  ></v-select>
                  <v-text-field
                    prepend-icon="person"
                    v-model="username"
                    label="Login"
                    type="text"
                    :rules="usernameRules"
                    required
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="lock"
                    v-model="password"
                    label="Password"
                    id="password"
                    type="password"
                    :rules="passwordRules"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-snackbar :color="snackBar.level" :timeout="4000" top="top" right="right"
                :success="snackBar.level === 'success'"
                :info="snackBar.level === 'info'" :warning="snackBar.level === 'warning'"
                :error="snackBar.level === 'error'" @input="closeSnackBar" :value="snackBar.value">
      {{ snackBar.text}}
      <v-btn flat="flat" @click="closeSnackBar" color="white">x</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
  import {listTenant, getJWT} from '@/api';
  import {mapState} from 'vuex';

  export default {
    name: 'Login',
    data: () => ({
      toolbar: {
        title: "Dalmore",
      },
      valid: true,
      tenantRules: [
        v => !!v || '主体不能为空',
      ],
      usernameRules: [
        v => !!v || '用户名不能为空',
      ],
      passwordRules: [
        v => !!v || '密码不能为空',
      ],
      tenant: null,
      username: null,
      password: null,
      tenants: [],
    }),
    computed: mapState([
      'snackBar',
    ]),
    methods: {
      closeSnackBar() {
        this.$store.dispatch('dismissSnackBar');
      },
      async listTenant() {
        const res = await listTenant({});
        const data = res.data.data;
        const tenants = data.tenants;
        this.tenants = [];
        tenants.forEach(value => {
          this.tenants.push({'text': value.name});
        });
      },
      async login() {
        if (this.$refs.form.validate()) {
          const res = await getJWT(
            {
              tenant: this.tenant.text,
              username: this.username.toLowerCase(),
              password: this.password
            }
          );
          if (res.data.status === 0) {
            this.$store.dispatch('login', res.data.data);
            const redirectURL = this.$route.query.redirect;
            if (redirectURL) {
              this.$router.push(redirectURL);
            } else {
              this.$router.push('/deploy/todo');
            }
          }
        }
      },
    },
    async mounted() {
      const isLoggedIn = !!localStorage.getItem('token');
      if (isLoggedIn) {
        const redirectURL = this.$route.query.redirect;
        if (redirectURL) {
          this.$router.push(redirectURL);
        } else {
          this.$router.push('/deploy/todo');
        }
      } else {
        this.listTenant();
      }
    },
  }
</script>

<style scoped>
</style>
