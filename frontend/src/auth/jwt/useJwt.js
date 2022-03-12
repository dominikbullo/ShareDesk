import axios from '@axios'
import JwtService from './jwtService'

function useJwt(axiosIns, jwtOverrideConfig) {
  const jwt = new JwtService(axiosIns, jwtOverrideConfig)
  return { jwt }
}

const { jwt } = useJwt(axios, {
  loginEndpoint: '/token/',
  registerEndpoint: '/users/register/',
  refreshEndpoint: '/token/refresh/',
  logoutEndpoint: '/logout/',
})
export default jwt
