import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'dogs',
    pathMatch: 'full'
  },
  {
    path: 'dogs',
    loadChildren: () => import('./dogs/dogs.module').then( m => m.DogsPageModule)
  },
  {
    path: 'cats',
    loadChildren: () => import('./cats/cats.module').then( m => m.CatsPageModule)
  },
  {
    path: 'others',
    loadChildren: () => import('./others/others.module').then( m => m.OthersPageModule)
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
